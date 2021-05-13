n, x = map(int,input().split())
m_list = []
for i in range(n):
  m_list.append(int(input()))

add = (x - sum(m_list)) // min(m_list)
print(n + add)