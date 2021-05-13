N, K = map(int, input().split())
h = [0]*N
for i in range(N):
  h[i] = int(input())
  
h = sorted(h)
hmin = max(h)
for i in range(N-K+1):
  hmin = min([hmin, h[i+K-1]-h[i]])
  
print(hmin)