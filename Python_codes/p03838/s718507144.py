#editorial
x,y=map(int, input().split())
ans=10**12
#00
if y-x>0:
    ans=min(ans,y-x)
#10
if y+x>=0:
    ans=min(ans,y+x+1)
#01
if -y-x>=0:
    ans=min(ans,-y-x+1)

if x-y>0:
    ans=min(ans,x-y+2)

print(ans)