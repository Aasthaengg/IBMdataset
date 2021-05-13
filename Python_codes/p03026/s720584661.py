n = int(input())
T = [[] for _ in range(n)]
for _ in range(n-1):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  T[a].append(b)
  T[b].append(a)
C = sorted(map(int, input().split()))
print(sum(C[:-1]))
L = [-1]*n
stack = [0]
while stack:
  temp = stack.pop()
  L[temp] = C.pop()
  for v in T[temp]:
    if L[v] == -1:
      stack.append(v)
print(*L)