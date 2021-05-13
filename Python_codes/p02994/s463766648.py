n,l=map(int,input().split())
sum_t=sum(range(l,l+n))
min_t=1000
for i in range(n):
    if min_t>=abs(l+i):
        ans=sum_t-l-i
        min_t=abs(l+i)
print(ans)