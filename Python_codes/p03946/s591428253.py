# 2019/10/09
# 解説かんにんぐ

n,t=map(int,input().split())
a=list(map(int,input().split()))
min_a=float('inf')
cost={}
for i in range(n):
    min_a=min(min_a,a[i])
    c=a[i]-min_a
    cost[c]=cost.get(c,0)+1
print(cost[max(cost.keys())])