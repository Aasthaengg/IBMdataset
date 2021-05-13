k,n=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
data=[0]*n
for i in range(n-1):
  data[i]=a[i+1]-a[i]
data[n-1]=k+a[0]-a[n-1]
print(sum(data)-max(data))