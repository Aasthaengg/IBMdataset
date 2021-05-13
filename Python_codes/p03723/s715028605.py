import sys
a,b,c=map(int,input().split())
if a%2==1 or b%2==1 or c%2==1:
    print(0)
    sys.exit(0)
elif a==b and b==c:
    print(-1)
    sys.exit(0)
ans=0
for i in range(1,10000):
    x=a//2
    y=b//2
    z=c//2
    a=y+z
    b=x+z
    c=x+y
    if a%2==1 or b%2==1 or c%2==1:
        ans=i
        break
print(ans)