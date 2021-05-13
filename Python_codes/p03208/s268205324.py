N,K = map(int,input().split())
h = [0]*N
hmax = 0
hmin = 0
H = [0]*(N-K+1)
for i in range(N):
  h[i] = int(input())
h.sort()
for i in range(N-K+1):
  hmin = h[i]
  hmax = h[i+K-1]
  H[i] = hmax-hmin
print(min(H))