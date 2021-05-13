N = int(input())
import math
U = math.ceil(3*N/4)
D = math.ceil(N/4)
if N % 2 == 0:
  ans = (N,N,N//2)
else:
  if D%2 == 1:
    D += 1
  h = -1
  for n in range(D,3500):
    if h > 0:
      break
    for w in range(n,3500):
      #print(h,n,w)
      if w*n*N/(4*n*w-w*N-n*N) == int(w*n*N/(4*n*w-w*N-n*N)):
        h = w*n*N//(4*n*w-w*N-n*N)
        ans = (w*n*N//(4*n*w-w*N-n*N),n,w)
        break
        
print(*ans)