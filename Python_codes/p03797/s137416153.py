n,m = map(int,input().split())
m_2 = m//2
ans = min(n,m_2)

if ans < m_2:
    make_s = m - ans*2
    ans += make_s // 4
    
print(ans)