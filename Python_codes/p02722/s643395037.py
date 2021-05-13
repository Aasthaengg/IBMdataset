N=int(input())
k=2
ans=1
factors=[]
i=1
while i*i<N-1:
  if (N-1)%i==0:
    ans+=1
  i+=1
while k*k<=N:
  n=0
  while pow(k,n)<=N:
    if (N-pow(k,n))%(pow(k,n+1))==0:
      ans+=1
      break
    n+=1
  k+=1
print(ans)