N, T = map(int, input().split())
t = list(map(int, input().split()))
ans = T
pre = 0
for ti in t[1:]:
  ans += min(T, ti - pre)
  pre = ti

print(ans)