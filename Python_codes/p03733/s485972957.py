N, T = map(int, input().split())
t = list(map(int, input().split()))

pt = t[0]
ans = 0
for ti in t[1:]:
    ans += min(ti-pt, T)
    pt = ti
print(ans+T)