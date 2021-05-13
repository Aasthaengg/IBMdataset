import sys
x,y=map(int,input().split())
tmp=x
ans=0
while tmp<=y:
    ans+=1
    tmp*=2
    if tmp>y:
        print(ans)
        sys.exit()