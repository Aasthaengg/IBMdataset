n,T =map(int, input().split())
ans = 10**5
for _ in range(n):
    c,t=map(int, input().split())
    if t > T:
        continue
    ans = min(ans,c)
if ans == 10**5:
    print("TLE")
else:
    print(ans)    