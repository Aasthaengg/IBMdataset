n,c,k=map(int,input().split())
data=[]
for i in range(n):
    data.append(int(input()))
data.sort()
i=0
count=0
while i <= n-1:
    j=i
    bus_join=0
    while bus_join < c and j <= n-1 and data[j]-data[i] <= k:
        j += 1
        bus_join += 1
    i=j
    count += 1
print(count)