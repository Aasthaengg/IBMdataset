n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
for i in range(n):
  z = v[i] - c[i]
  ans = max(ans, ans+z)
print(ans)