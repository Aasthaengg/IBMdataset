N=int(input())
a=[int(x) for x in input().split()]
b=a
t=-1
s=0
while s==0:
  for i in range(N):
    if b[i]%2!=0:
      s=1
    b[i]=b[i]/2
  t=t+1
    
print(t)