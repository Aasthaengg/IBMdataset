x,y=map(int,input().split())
ans=0
if x in [1,2,3]:
    ans+=(4-x)*100000
if y in [1,2,3]:
    ans+=(4-y)*100000
if x==1 and y==1:
    ans+=400000
print(ans)