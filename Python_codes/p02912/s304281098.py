n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
c=0
while c<m:
  d=a[0]/2
  for i in range(n):
    if a[0]==0:
      c=m
    if a[i]>d:
      a[i]//=2
      c+=1
      if c==m:
        break  
    else:
      a.sort(reverse=True)
      break
print(sum(a))