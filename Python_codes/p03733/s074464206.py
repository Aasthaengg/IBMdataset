N, T = map(int,input().split())
t = list(map(int,input().split()))
ans = 0
s, e = 0, T
for k in range(1,N):
    if e < t[k]:
        ans += e-s
        s = t[k]
        e = t[k] + T
    else:
        e = t[k] + T
ans += e-s
print(ans)
