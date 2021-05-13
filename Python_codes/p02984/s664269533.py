n = int(input())
d_ls = list(map(int, input().split()))
m_0 = 0
for i in range(n):
    if i % 2 == 0:
        m_0 += d_ls[i]
    else:
        m_0 -= d_ls[i]
m_ls = [0] * n
m_ls[0] = m_0
for i in range(n-1):
    m_ls[i+1] = 2*d_ls[i] - m_ls[i]
m_ls = list(map(str,m_ls))
print(' '.join(m_ls))

