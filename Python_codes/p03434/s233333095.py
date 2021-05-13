N = int(input())
a = list(map(int, input().split()))

A = 0
B = 0
while True:
  m_a = max(a)
  A += m_a
  a.remove(m_a)
  if len(a) == 0: break
  
  m_b = max(a)
  B += m_b
  a.remove(m_b)
  if len(a) == 0: break

print(A-B)