N=int(input())
a=list(map(int,input().split()))
p,q,r=0,0,0
for i in range(N):
  if a[i]%2==0:
    if a[i]%4==0:
      r+=1
    else:
      q+=1
  else:
    p+=1
if p-1<r:
  print('Yes')
elif p-1==r:
  if q==0:
    print('Yes')
  else:
    print('No')
else:
  print('No')