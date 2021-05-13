n,a,b=map(int,input().split())
x=list(map(int,input().split()))
y=[(x[i+1]-x[i])*a for i in range(n-1)]
hirou=0
for i in range(n-1):
  hirou+=min(y[i],b)
print(hirou)