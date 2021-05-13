n,T=map(int,input().split())
cost=10000
for i in range(n):
    c,t=map(int,input().split())
    if t<=T:
        cost=min(cost,c)
print(cost if cost!=10000 else "TLE")
