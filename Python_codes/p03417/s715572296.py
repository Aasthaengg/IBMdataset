N, M = [int(x) for x in input().split()]
def sol(N,M):
  if N==0 or M==0:
      return 0
  elif N==1 or M==1:
    return abs(abs(N-M)-1)
  x = (abs(3-N)+1)*(M-2)
  y = (abs(3-M)+1)*abs((N-2))
  return min(x,y)

print(sol(N,M))