a,b=map(int,input().split())
ans=0
for x in range(a+1):
    #y+z=b-x
    minn=min(a,b-x)
    for y in range(minn+1):
        z=b-x-y
        if 0<=z and z<=a:
            ans+=1
print(ans)
