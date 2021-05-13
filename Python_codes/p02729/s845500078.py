n,m = map(int,input().split())

if n == 1 or n == 0 :
  n_c = 0
else :
  n_c = n * (n-1) / 2
if m == 1 or m == 0 :
  m_c = 0
else :
  m_c = m * (m-1) / 2

print(int(n_c + m_c))