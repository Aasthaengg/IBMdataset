n, k = map(int, input().split())
arr = []
for i in range(n):
  c = i + 1
  p = 1 / n
  while 1 <=  c <= k - 1:
    c *= 2
    p *= 0.5
  arr.append(p)
ans = sum(arr)
print(ans)