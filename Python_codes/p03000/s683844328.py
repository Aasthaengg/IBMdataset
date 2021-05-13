k=0
s=0
a,b=map(int,input().split())
L=list(map(int,input().split()))
for i in range(a):
  s+=L[i]
  if s<=b:
    k+=1
print(k+1)