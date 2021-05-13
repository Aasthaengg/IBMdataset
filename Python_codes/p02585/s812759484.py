N,K=map(int,input().split())
P=[int(x)-1 for x in input().split()]
C=[int(x) for x in input().split()]

def circle_grouping(P):
  P_in=[]
  P_group=[]
  for i in range(N):
    if i in P_in:
      pass
    else:
      start=i
      j=P[i]
      ls=[i]
      P_in.append(i)
      while j!=start:
        ls.append(j)
        P_in.append(j)
        j=P[j]
      P_group.append(ls)
  return P_group

def circle_maximum(A,K):
  max_val=max(A)
  for i in range(len(A)):
    val=0
    for k in range(K):
      pos=(i+k)%len(A)
      val+=A[pos]
      max_val=max(max_val,val)
  return max_val

score=max(C)
P_group=circle_grouping(P)
for A in P_group:
  k_rem=K%len(A)
  cycle=K//len(A)
  if cycle>=1:
    k_rem+=len(A)
    cycle-=1
  B=[C[i] for i in A]
  score=max(score,max(0,sum(B))*cycle+circle_maximum(B,k_rem))
print(score)