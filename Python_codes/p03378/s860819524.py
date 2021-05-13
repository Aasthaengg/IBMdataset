n,m,x=map(int,input().split())
a=[int(i) for i in input().split()]
cost=0
for i in range(x,n):
    if i in a:
        cost+=1
cost2=0
for i in range(0,x+1)[::-1]:
    if i in a:
        cost2+=1
print(min(cost,cost2))