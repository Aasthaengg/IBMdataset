r=0
a,b=map(int,input().split())
L=list(map(int,input().split()))
for i in range(a):
  if L[i]>=b:
    r+=1
print(r)