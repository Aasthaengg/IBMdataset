def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
from itertools import combinations_with_replacement
N,M,Q=MI()
A=[]
B=[]
C=[]
D=[]
ans=0
for i in range(Q):
  a,b,c,d=MI()
  a-=1
  b-=1
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)
#print(A,B,C,D)
Num=list(range(1,M+1))
#print(Num)
#print(list(combinations(Num,N)))
for j in list(combinations_with_replacement(Num,N)):
  tmp=0
  for i in range(Q):
    if j[B[i]]-j[A[i]]==C[i]:
      tmp+=D[i]
  ans=max(ans,tmp)  
print(ans)