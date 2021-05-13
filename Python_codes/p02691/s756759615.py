N=int(input())
A=list(map(int,input().split()))
import collections
B=[]
C=[]
for i,a in enumerate(A):
  B.append(a-i)
  C.append(-a-i)
C=collections.Counter(C)
ans=0
for b in B:    
  ans+=C[b]
print(ans)