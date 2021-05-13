N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

if P == Q:
  print(0)
  exit(0)
  
import itertools as it

S = list(it.permutations(range(1,N+1)))
pi,qi = -10,-10
for i in range(len(S)):
  if S[i] == P:
    pi = i
  elif S[i] == Q:
    qi = i
  if pi >= 0 and qi >= 0:
    break

ans = abs(pi-qi)
print(ans)