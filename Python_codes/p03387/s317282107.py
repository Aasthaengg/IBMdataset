a = list(map(int, input().split()))
s, m, b = sorted(a)
cnt = 0
m_s = m - s
cnt += b - m
cnt += m_s // 2

if m_s % 2 == 1:
    cnt += 2
print(cnt)
