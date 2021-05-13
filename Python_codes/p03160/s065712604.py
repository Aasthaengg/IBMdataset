n=int(input())
h=[int(x) for x in input().split()]
a=[0]*n
a[1]=abs(h[0]-h[1])

for i in range(2,n):
  a[i]=min(a[i-2]+abs(h[i]-h[i-2]),a[i-1]+abs(h[i]-h[i-1]))
  
print(a[n-1])