N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
 
def isfeasible(L):
  k = 0
  for a in A:
    if a < L:
      break
    if a%L == 0:
      dk = a//L - 1
    else:
      dk = a//L
    k += dk
    if k > K:
      return False
  return True
 
l = 0
r = A[0]

while r-l>1:
  L = (r+l)//2
  if isfeasible(L):
    r = L
  else:
    l = L
print(r)