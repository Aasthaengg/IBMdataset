N, C = map(int, input().split())
V = [0]
X = [0]
Y = []
for i in range(N):
  x, v = map(int, input().split())
  X += [x]
  Y += [C-x]
  V += [v]
Y += [0]
f = [0]
g = [0]
for i in range(1,N+1):
  f += [f[-1]+X[i-1]+V[i]-X[i]]
  g += [g[-1]+Y[N-i+1]+V[N-i+1]-Y[N-i]]
g = g[::-1]

m = -1
ans1 = 0
for i in range(N+1):
  if m<f[i]:
    m = f[i]
  ans1 = max(ans1, m+g[i]-Y[i])

m = -1
ans2 = 0
for i in range(N, -1, -1):
  if m<g[i]:
    m = g[i]
  ans2 = max(ans2, m+f[i]-X[i])

print(max(ans1, ans2))