import itertools

A=list(map(int, input().split()))

p = list(itertools.permutations(range(3) ) )     

cst=sum(A)
for i in range(3):
  c=abs(A[p[i][1]]-A[p[i][0]])+abs(A[p[i][2]]-A[p[i][1]])
  if c<=cst:
    cst=c
print(cst)