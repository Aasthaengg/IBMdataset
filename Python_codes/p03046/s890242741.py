m,k=map(int,input().split())
if k>=(2**m):
  print(-1)
elif m==1:
  if k==0:
    print(0,0,1,1)
  else:
    print(-1)
elif k==0:
  print(" ".join(map(str,[i//2 for i in range(2**(m+1))])))
else:
  l=[i+int(i>=k) for i in range(1,2**m-1)]
  ll=[i+int(i>=k) for i in range(2**m-2,0,-1)]
  ans=[k]+l+[k,0]+ll+[0]
  print(" ".join(map(str,ans)))