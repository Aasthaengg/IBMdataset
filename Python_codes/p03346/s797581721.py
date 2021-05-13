n=int(input())

a=[int(input())-1 for _ in range(n)]
posi=[0]*n

for i in range(n):
    posi[a[i]]=i

cnt=0
ans=0
p=0

for i in range(n):
    if p<=posi[i]:
        cnt+=1
        p=posi[i]
        ans=max(ans,cnt)
    else:
        p=posi[i]
        cnt=1
    #print(i+1,ans)


print(n-ans)