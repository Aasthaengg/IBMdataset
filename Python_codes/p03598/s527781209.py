n=int(input())
k=int(input())
x=list(map(int,input().split()))
sum=[]
for i in range(n):
    if k-x[i]>=x[i]:
        sum.append(2*x[i])
    else:
        sum.append(2*(k-x[i]))
ans=0
for i in range(n):
    ans+=sum[i]
print(ans)