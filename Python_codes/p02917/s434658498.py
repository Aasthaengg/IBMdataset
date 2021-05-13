n=int(input())
b=list(map(int,input().split()))
a=[0 for _ in range(n)]
for i in range(n):
  if i==0:
    a[i]=b[0]
  elif i==n-1:
    a[i]=b[n-2]
  else:
    a[i]=(min(b[i-1], b[i]))
print(sum(a))