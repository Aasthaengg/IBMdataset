n, k = map(int, input().split())
p = list(map(int, input().split()))
e = []
m = 0
arr = []
ans = 0
for i in range(n):
  m += (p[i] + 1) / 2
  e.append(m)
arr.append(e[k - 1])
for i in range(n - k):
  arr.append(e[i + k] - e[i])
ans = max(arr)
print(ans)