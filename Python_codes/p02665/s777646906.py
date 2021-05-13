N = int(input())
A = list(map(int, input().split()))
  
def solve(N, A):
  
  if N == 0 and A[0] > 1 or N > 0 and A[0] > 0:
    print(-1)
    return

  total = sum(A[1:])
  #t = A[-1] + A[-2]
  par = 1 - A[0]
  rt = 1
  for i, a in enumerate(A[1:]):
    total -= a
    max_node = par * 2
    cur = max_node - a
    if cur < 0:
      print(-1)
      return
    cur = min(total, cur)
    #print(i+1, a, cur)
    rt += a
    if i + 1 < N:
      rt += cur
    par = cur  
   
  print(rt)
  
solve(N, A)

