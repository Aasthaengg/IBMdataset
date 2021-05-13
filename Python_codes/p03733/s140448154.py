N,T = map(int,input().split())
ts = list(map(int,input().split()))

ans = 0
until = 0
for t in ts:
    ans += min(T, t+T-until)
    until = t+T
print(ans)