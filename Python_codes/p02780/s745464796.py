import itertools
n,k=map(int,input().split())
p=list(map(int,input().split()))
l=[]
for i in range(n):
    exp=(p[i]+1)/2
    l.append(exp)
cumsum=[0]+list(itertools.accumulate(l))
ans=0
for i in range(n-k+1):
    sum_num=cumsum[i+k]-cumsum[i]
    if sum_num>ans:
        ans=sum_num
print(ans)