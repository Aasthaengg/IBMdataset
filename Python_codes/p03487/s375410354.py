n=int(input())
a=list(map(int,input().split()))
x=[0]*(10**5+1)
ans=0
for i in range(n):
    if a[i]>10**5:
        ans+=1
    else:
        x[a[i]]+=1
for i in range(1,10**5+1):
    if x[i]<i:
        ans+=x[i]
    else:
        ans+=x[i]-i
print(ans)
