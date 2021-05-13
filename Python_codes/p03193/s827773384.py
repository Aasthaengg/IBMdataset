li = list(map(int,input().split()))
ans=0
for i in range(li[0]):
    x,y = map(int,input().split())
    if x>=li[1] and y>=li[2]:
        ans+=1
print(ans)
