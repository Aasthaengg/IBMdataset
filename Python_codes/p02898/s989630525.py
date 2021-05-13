n, k = map(int, input().split())
lst = list(map(int, input().split()))
res = 0
for i in range(n):
  if lst[i] >= k:
    res += 1
print(res)