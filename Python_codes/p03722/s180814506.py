n, m = map(int, input().split())
list_edge = []
for _ in range(m):
  a, b, c = map(int, input().split())
  list_edge.append((a-1, b-1, -c))

list_point = [float("inf") if i != 0 else 0 for i in range(n)]
for i in range(n+1):
  for a, b, c in list_edge:
    if list_point[a] != float("Inf") and list_point[b] > list_point[a] + c:
      list_point[b] = list_point[a] + c
      if i == n and b == n-1:
        print("inf")
        exit()
print(-1 * list_point[-1])