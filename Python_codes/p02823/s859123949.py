n,a,b=map(int,input().split())
if b<a:b,a=a,b
ans=float("inf")
if abs(a-b)%2==0:print(abs(a-b)//2)

else:
    print(min(n-b+1,a)+abs(b-a-1)//2)