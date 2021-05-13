n = int(input())
v = [int(k) for k in input().split()]
c = [int(k) for k in input().split()]
ans = 0
for i in range(n):
  a = v[i]-c[i]
  if a > 0:
    ans += a
print(ans)