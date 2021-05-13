n,k=map(int,input().split())

cost=[0 for i in range(n)]

h=list(map(int,input().split()))


for i in range(1,n):
    q=1e100
    r=1000
    for j in range(i-1,i-min(k,i)-1,-1):
        if q>cost[j]+abs(h[i]-h[j]) :
            q=abs(h[i]-h[j])+cost[j]
    cost[i]=q   


print(cost[-1])
