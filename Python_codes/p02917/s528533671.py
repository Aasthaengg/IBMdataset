n=int(input())
b=list(map(int,input().split()))
b.reverse()

a=[0]*n

for i in range(1,n-1):
  a[i]=min(b[i],b[i-1])

a[0]=b[0]
a[n-1]=b[n-2]

print(sum(a))