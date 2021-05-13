n=int(input())
a=list(map(int,input().split()))
d=100
ans=1000
av=sum(a)/n
for i in range(n):
    res=abs(a[i]-av)
    if res<d:
        d=res
        ans=i
print(ans)