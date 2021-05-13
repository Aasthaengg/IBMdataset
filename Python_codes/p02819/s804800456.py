n=int(input())
for i in range(n,n+1000):
  flg=0
  for j in range(2,int(i**(1/2))+1):
    if i%j==0:
      flg=1
  if flg==0:
    print(i)
    break