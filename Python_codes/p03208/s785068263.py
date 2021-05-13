N,K=map(int,input().split())
h=[int(input()) for _ in range(N)]

h=sorted(h)

MIN=10**10
for i in range(N-K+1):
  tmp = h[i+K-1]-h[i]
  if tmp < MIN:
    MIN = tmp
    
print(MIN)