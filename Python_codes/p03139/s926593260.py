n,a,b=map(int,input().split())
x=min(a,b)
if a+b<=n:
    y=0
else:
    y=a+b-n
print(x,y)

