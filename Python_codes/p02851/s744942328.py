from collections import Counter
N,K=map(int,input().split())
A=list(map(int,input().split()))

A=list(map(lambda x:x%K-1,A))
sa=[0]*(N+1)
for i in range(1,N+1):
  sa[i]=(sa[i-1]+A[i-1])%K

c=Counter(sa[:K-1])

ans=0
for i in c.values():
  ans+=i*(i-1)//2
  
for i in range(K-1,N+1):
  ans+=c[sa[i]]
  c[sa[i-(K-1)]]-=1
  c[sa[i]]+=1

  
print(ans)