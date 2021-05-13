N = int(input())

fact_ct = [0 for _ in range(N+1)]
pr = []

def primes():
  ans = set()
  visited = set()
  for p in range(2,N+1):
    if p in visited:
      continue
    ans.add(p)
    q = p
    while q <= N:
      visited.add(q)
      q += p    
  return ans

pr = primes() 

def add_fact_ct(n):
  visited = set()
  for p in range(2,N+1):
    if p not in pr:
      continue
    while n % p == 0:
      fact_ct[p] += 1
      n //= p  

for n in range(2, N+1):
  add_fact_ct(n)
  
ct_75 = 0
ct_25 = 0
ct_15 = 0
ct_5 = 0
ct_3 = 0
ct_1 = 0
  
for ct in fact_ct:
  if ct >= 74:
    ct_75 += 1
  if ct >= 24:
    ct_25 += 1
  if ct >= 14:
    ct_15 += 1
  if ct >= 4:
    ct_5 += 1 
  if ct >= 2:
    ct_3 += 1

ans = 0

ans += ct_75

ans += ct_25 * (ct_3-1)
ans += ct_15 * (ct_5-1)

ans += ct_5*(ct_5-1)*(ct_3-2) // 2

print(ans)
#print(fact_ct) 
