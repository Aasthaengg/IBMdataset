import math
n = float(input())
m_low = math.ceil(n / 1.08)
m_high = math.floor((n+1)/1.08)
if m_low > m_high:
  print(':(')
else:
  ch_low = math.floor(m_low*1.08)
  ch_high = math.floor(m_high*1.08)
  if ch_low == int(n):
    print(m_low)
  elif ch_high == int(n):
    print(m_high)
  else:
    print(':(')