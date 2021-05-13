n=int(input())
a=list(map(int,input().split()))
sum_r=sum(a)
sum_l=0
ans=10**20
for i in range(n-1):
    sum_l+=a[i]
    sum_r-=a[i]
    if abs(sum_r-sum_l)<ans:
        ans=abs(sum_r-sum_l)
print(ans)
