n,m=map(int, input().split())
if n>=m/2:
    m_fin = m//2
    print(m_fin)
else:
    m_aft = m -2*n
    m_fin = m_aft//4
    print(n+m_fin)