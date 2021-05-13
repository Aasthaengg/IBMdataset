n,*a=map(int,open(0).read().split())
count=[0]*n
for i in range(n-1):
    count[a[i]-1]+=1
for i in range(n):
    print(count[i])