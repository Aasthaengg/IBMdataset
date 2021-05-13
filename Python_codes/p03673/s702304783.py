n=int(input())
a=list(map(int,input().split()))

kisu=[]
gusu=[]
for x in range(n):
  if (x+1)%2==1:
    kisu.append(a[x])
  else:
    gusu.append(a[x])
    
if n%2==0:
  gusu.reverse()
  ans=gusu+kisu
  
else:
  kisu.reverse()
  ans=kisu+gusu
  
ans1=[str(f) for f in ans]

ans1=' '.join(ans1)

print(ans1)