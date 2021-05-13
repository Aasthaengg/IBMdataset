n=int(input())
l=list(map(int,input().split()))
l.sort()
ans=0
for i in range(n):
  for j in range(i+1,n):
    kmax=n
    kmin=j
    while True:
      k=(kmax+kmin)//2
      if l[i]+l[j]>l[k]:
        ans=ans+k-kmin
        kmin=k
      else:
        kmax=k
      if kmax-kmin==1:
        break
print(ans)