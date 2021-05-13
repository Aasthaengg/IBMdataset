N,x=input().split()
X=int(x)
n=int(N)
y=0
A = [int(i) for i in input().split()]
A.sort()
for z in range(n):
  y+=A[z]
  if y>=X:
    if y==X:
      print(z+1)
    else:
      print(z)
    break
else:
  print(n-1)