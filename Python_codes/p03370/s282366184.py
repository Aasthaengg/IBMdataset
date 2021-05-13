#-------------
N, X = map(int, input().split())
m = [int(input()) for l in range(N)]
#-------------

base = 0
for i in range(N):
  base += m[i]
  
remain = X - base
m_min = min(m)

Y = remain//m_min

print(N+Y)