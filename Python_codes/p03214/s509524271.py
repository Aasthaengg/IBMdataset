n=int(input())
a=list(map(int,input().split()))

r=sum(a)/n
m=10000
ans=0
for i in range(n):
    if m>abs(a[i]-r):
        m=abs(a[i]-r)
        ans=i
print(ans)