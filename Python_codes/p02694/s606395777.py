x=int(input())
ans=0
cost=100
while(cost<x):
    cost=cost*101//100
    ans+=1
print(ans)