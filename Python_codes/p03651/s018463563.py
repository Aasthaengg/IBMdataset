from functools import reduce

def gcd(a,b):
  while b:
    c = a%b
    a = b
    b = c    
  return a

n,k = map(int,input().split())
A = list(map(int,input().split()))

ans = 'IMPOSSIBLE'  

if max(A) < k:
  pass
else:  
  m = reduce(gcd,A)
  for i in range(n):
    if (k-A[i])%m == 0:
      ans = 'POSSIBLE'
      break
  
print(ans)    