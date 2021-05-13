n = int(input())
p_mn = m_mn= 10**9 * 2
p_mx = m_mx = -p_mn
for i in range(n):
    x, y = map(int, input().split())
    p = x + y
    m = x - y
    p_mx = max(p_mx, p)
    p_mn = min(p_mn, p)
    m_mx = max(m_mx, m)
    m_mn = min(m_mn, m)
print(max(p_mx-p_mn, m_mx-m_mn))
