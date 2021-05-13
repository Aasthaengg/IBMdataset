N , T = map(int,input().split())
ans = 10**4
for i in range(N):
    c , t = map(int,input().split())
    if t <= T:
        ans = min(c,ans)
if ans == 10**4:
    print("TLE")
else:
    print(ans)