n=int(input())
l=list(map(int,input().split()))
max=l[0]
ans=0
for i in range(1,len(l)):
    if l[i]<max:
        ans+=(max-l[i])
    else:
        max=l[i]
print(ans)