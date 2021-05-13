n,*a=map(int,open(0))
c=0
for i in range(n-1,0,-1):
  if a[i]-a[i-1]>1:
    print(-1)
    exit()
  if a[i]<=a[i-1]:
    c+=a[i]
  else:
    c+=1
print(-(a[0]>0)or c)