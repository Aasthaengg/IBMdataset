n = int(input())
arr = list(map(int, input().split()))
l = []
for i in range(n):
  for j in range(n):
    if i != j:
      l.append(arr[i] * arr[j])
print(sum(l) // 2)