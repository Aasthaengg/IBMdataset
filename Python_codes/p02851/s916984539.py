N,K=map(int,input().split())
A=list(map(int,input().split()))
for i in range(N):
  A[i] -= 1
  A[i] %= K

hm = {}
hm[A[0]] = 1
out = 0
for i in range(1,N):
  A[i] += A[i-1]
  A[i] %= K

for i in range(min(K-1,N)):
  if A[i]==0 and K != 1:
    out+=1
    
for i in range(1,min(N,K)):
  if A[i] in hm:
    hm[A[i]]+=1
  else:
    hm[A[i]]=1
  out += hm[A[i]]-1
  
for i in range(min(K,N),N):
  if A[i] in hm:
    hm[A[i]]+=1
  else:
    hm[A[i]]=1
  hm[A[i-K]] -= 1
  out += hm[A[i]]-1

print(int(out))