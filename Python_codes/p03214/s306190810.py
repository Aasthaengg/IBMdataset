n=int(input())
a=list(map(int,input().split()))
m=sum(a)/len(a)
tmp=10**3
ans=0
for i in range(n):
    if abs(a[i]-m)<tmp:
        ans=i
        tmp=abs(a[i]-m)
print(ans)