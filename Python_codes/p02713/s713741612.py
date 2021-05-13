K = int(input())

def gcd(p, q):
  r = p % q
  if r == 0:
    return q
  else:
    p = q
    q = r
    return gcd(p, q)

total = 0
for i in range(1,K+1,1):
  for j in range(1,K+1,1):
    p = gcd(i,j)
    for k in range(1,K+1,1):
      q = gcd(k, p)
      total += q
print(total)
      
