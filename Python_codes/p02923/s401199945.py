x=int(input())
s=list(map(int,input().split()))

res=0
sm=0

cur=s[0]

for n in range(1,x):
    if s[n]<=cur:
        cur=s[n]
        sm+=1
    else:
        cur=s[n]
        res=max(res,sm)
        sm=0
res=max(res,sm)
print(res)