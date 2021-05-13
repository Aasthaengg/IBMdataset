n=int(input())
a=list(map(int,input().split()))
b0=[]
b1=[]
for i in range(n):
  if i%2==0:
    b0.append(a[i])
  else:
    b1.append(a[i])
if n%2!=0:
  b0=list(reversed(b0))
  b=b0+b1
  print(' '.join(map(str, b)))
else:
  b1=list(reversed(b1))
  b=b1+b0
  print(' '.join(map(str, b)))
