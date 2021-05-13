n=int(input())
b =list(map(int, input().split()))
a = [0 for _ in range(n)]

for i in range(n-1):
  if i==0:
    a[i]=b[i]
    a[i+1]=b[i]
  elif b[i]>b[i-1]:
    a[i+1]=b[i]
  else:
    a[i]=b[i]
    a[i+1]=b[i]
print(sum(a))