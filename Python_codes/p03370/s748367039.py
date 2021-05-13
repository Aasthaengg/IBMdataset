n,x=map(int,input().split())
ma=float(1001)
for i in range(n):
    m=int(input())
    x-=m
    ma=min(ma,m)
print(n+x//ma)