n,lim = map(int,input().split())

ans = 10000

for i in range(n):
    cost,time = map(int,input().split())
    
    if time <= lim and cost < ans:
        ans = cost

if ans == 10000:
    print("TLE")
else:
    print(ans)