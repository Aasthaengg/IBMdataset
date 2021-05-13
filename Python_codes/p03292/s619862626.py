a=list(map(int,input().split()))
a.sort()
cost=0
cost+=abs(a[0]-a[1])
cost+=abs(a[1]-a[2])
print(cost)