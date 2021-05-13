a,b=map(int,input().split())
L=list(map(int,input().split()))
s=0
if L[0]>b:
  s+=L[0]-b
  L[0]=b
for i in range(1,a):
  if L[i-1]+L[i]>b:
    s+=L[i]-b+L[i-1]
    L[i]=b-L[i-1]
print(s)