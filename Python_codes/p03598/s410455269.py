n=int(input())
k=int(input())
x=[int(i)for i in input().split()]
cost=sum([min(i,k-i)*2 for i in x])
print(cost)