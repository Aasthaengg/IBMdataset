n=int(input())
v=list(map(int, input().split()))
c=list(map(int, input().split()))
res =0
for i in range(n):
    cost=v[i]-c[i]
    if cost >0:res+=cost
print(res)