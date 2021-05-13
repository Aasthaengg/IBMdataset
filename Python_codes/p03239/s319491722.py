n,k=map(int,input().split())
c=1000000
for i in range(n):
    x,y=map(int,input().split())
    if(y<=k):
        c=min(c,x)
if(c==1000000):
    print("TLE")
else:
    print(c)