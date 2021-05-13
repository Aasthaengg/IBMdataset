n=int(input())
a=list(map(int, input().split()))

md=sum(a)/n
dist=float("inf")
ans=float("inf")
for i in range(n):
    if abs(a[i]-md)<dist:
        ans=i
        dist=abs(a[i]-md)
print(ans)
