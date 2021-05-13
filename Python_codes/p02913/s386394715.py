n=int(input())
s=list(input())

def Z_algorithm(s):
  N=len(s)
  Z_alg=[0]*N
  Z_alg[0]=N
  i=1
  j=0
  while i<N:
    while i+j<N and s[j]==s[i+j]:
      j+=1
    Z_alg[i]=j
    if j==0:
      i+=1
      continue
    k=1
    while i+k<N and k+Z_alg[k]<j:
      Z_alg[i+k]=Z_alg[k]
      k+=1
    i+=k
    j-=k
  return Z_alg

ans=0
for i in range(n):
  S=s[i:n]
  z=Z_algorithm(S)
  for j in range(len(z)):
    if z[j]<=j:
      if ans<z[j]:
        ans=z[j]
print(ans)