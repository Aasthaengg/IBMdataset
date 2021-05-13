n = int(input())
a = list(map(int, input().split()))
ue = [0]*10**6
sita = [0]*10**6
for i in range(n):
  if i % 2 == 0:
    ue[a[i]] += 1
  else:
    sita[a[i]] += 1

m_ue = max(ue)
m_ue_idx = ue.index(m_ue)
m_sita = max(sita)
m_sita_idx = sita.index(m_sita)
if m_ue_idx != m_sita_idx:
  print(n - m_ue - m_sita)
else:
  s_ue = sorted(ue, reverse=True)
  s_sita = sorted(sita, reverse=True)
  print(min(n-s_ue[0]-s_sita[1], n-s_ue[1]-s_sita[0]))
