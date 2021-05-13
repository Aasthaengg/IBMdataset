N,K = map(int,input().split())

p = 0
q = 0
for j in range(N,0,-1):
  while j*(2**q) < K:
    q += 1
  p += 0.5**q
print(p*(1/N))