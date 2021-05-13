import sys
N=int(input())
S=input()

def z_alg(S):
  N=len(S)
  Z=[N]+[0]*(N-1)
  i,j=1,0
  while i<N:
    while i+j<N and S[j]==S[i+j]:
      j+=1
    if not j:
      i+=1
      continue
    Z[i]=j
    k=1
    while N-i>k and k<j-Z[k]:
      Z[i+k]=Z[k]
      k+=1
    i+=k
    j-=k
  return Z

answer=0
for i in range(N):
  zlist=z_alg(S[i:])
  #print(i,S[i:],zlist)
  for j in range(N-i):
    if j>=zlist[j] and answer<zlist[j]:
      answer=zlist[j]
      
print(answer)