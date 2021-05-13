N=int(input())
K=int(input())

mi=100000
s=1
for i in range(N+1):
  s=2**i+K*(N-i)
  mi=min(mi,s)
print(mi)