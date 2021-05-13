n,a,b= map(int,input().split())
x= list(map(int,input().split()))
cost=0
for i in range(n-1):cost+=min(b,a*(x[i+1]-x[i]))
print(cost)