import sys
a,b,c=map(int,input().split())
ans=0
if a%2==1 or b%2==1 or c%2==1:
    print(0)
    sys.exit()
if a%2==0 and a==b==c:
    print(-1)
    sys.exit()
while a%2==0 and b%2==0 and c%2==0:
    ta=a/2
    tb=b/2
    tc=c/2
    a=tb+tc
    b=ta+tc
    c=ta+tb
    ans+=1
print(ans)