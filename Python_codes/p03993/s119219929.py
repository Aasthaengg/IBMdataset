n=int(input())
a=list(map(int,input().split()))
l=[[] for i in range(n)]
ans=0
for i in range(n):
    l[a[i]-1].append(i)
    if a[i]-1 in l[i]:
        ans+=1
print(ans)