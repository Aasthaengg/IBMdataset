N = int(input())
l = 0
r = (N - 1)
m = (l + r) // 2

print(l)
l_stat = input()
if l_stat == "Vacant":
  exit()

print(m)
m_stat = input()
if m_stat == "Vacant":
  exit()

while True:
  if ((m - l) % 2 == 0 and l_stat == m_stat) or ((m - l) % 2 == 1 and l_stat != m_stat):
    l, m = m, (m + r + 1) // 2
    l_stat = m_stat
    print(m)
    m_stat = input() 
    if m_stat == "Vacant":
      exit()
  else:
    m, r = (l + m) // 2, m
    print(m)
    m_stat = input()
    if m_stat == "Vacant":
      exit()
