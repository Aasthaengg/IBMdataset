N=int(input())
a=[int(i) for i in input().split()]
M = max(a)
m = min(a)
print(2*N-1)
if abs(M) > abs(m):
  Mi = a.index(M)
  for i in range(N):
    print(Mi+1,i+1)
  for i in range(N-1):
    print(i+1,i+2)
else:
  mi = a.index(m)
  for i in range(N):
    print(mi+1,i+1)
  for i in range(N-1)[::-1]:
    print(i+2,i+1)