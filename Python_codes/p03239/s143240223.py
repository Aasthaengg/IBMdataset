N,T=map(int,input().split())
cost=10**9
for _ in range(N):
    c,t=map(int,input().split())
    if t<=T:
        cost=min(cost,c)
if cost==10**9:
    print("TLE")
else:
    print(cost)