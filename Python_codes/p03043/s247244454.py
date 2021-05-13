n,k = map(int,input().strip().split())
c = 0
for i in range(1,n+1):
  if i>k:
    c+=1/n
  else:
    cnt=0
    while i<k:
      i*=2
      cnt+=1
    c+=1/n*(1/2)**cnt
print(c)
