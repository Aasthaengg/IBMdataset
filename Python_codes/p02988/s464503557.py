n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(1,n-1):
    l=[]
    l.append(a[i-1])
    l.append(a[i])
    l.append(a[i+1])
    l.sort()
    if l[1]==a[i]:
        ans+=1
print(ans)