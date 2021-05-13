N = int(input())

ts = [0]*N
ms = [0]*N
for i in range(N):
  t_i, m_i = input().split()
  m_i = int(m_i)
    
  ts[i] = t_i
  ms[i] = m_i
    
X = input()

ind = ts.index(X)
ind_m = ms[ind]
ans = sum(ms[ind:]) - ind_m

print(ans)