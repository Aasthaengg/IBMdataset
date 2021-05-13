import sys
n,k = map(int,input().split())
a = list(map(int,input().split()))
cost = [0] * n
cost[1] = abs(a[1]-a[0])
mi = sys.maxsize
for i in range(1,n):
    for j in range(max(0,i-k),i):
        mi = min(mi,cost[j]+abs(a[i]-a[j]))
        #print(j,mi)
    
    cost[i] = mi
    mi = sys.maxsize
#print(cost)
print(cost[n-1])