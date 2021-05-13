x,y = list(map(int, input().split()))
ans=0
if abs(x) < abs(y):
    if x<0:
        ans+=1
    ans+=abs(y)-abs(x)
    if y<0:
        ans+=1
elif abs(x) > abs(y):
    if x>0:
        ans+=1
    ans+=abs(x)-abs(y)
    if y>0:
        ans+=1
else:
    if x!=y:
        ans+=1
print(ans)