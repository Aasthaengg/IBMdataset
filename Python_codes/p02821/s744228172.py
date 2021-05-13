#149_E. 2分探索. 神.ちょい変えた版





















N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A.sort()
A.reverse()

def PairCount_and_TotalSum_over(x):
  c,k,si,i = [0,0,0,0]
  for j in reversed(range(N)):
    while i<N and A[i]+A[j]>=x:
      si += A[i]
      i += 1
    c += i
    k += si + A[j]*i
    
  return (c, k)

def binary_search(l, u):
  m = (l+u)//2
  c, k = PairCount_and_TotalSum_over(m)
  if c<M:
    return binary_search(l, m)
  else:
    if l==m:
      print(k-(c-M)*l)
    else:
      return binary_search(m, u)

binary_search(0, A[0]*2+1)
