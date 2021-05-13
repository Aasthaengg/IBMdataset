N = int(input())
A = list(map(int,input().split()))

p,m = [],[]
p_total = 0
m_total = 0
p_max,p_min = 0,10**10
m_max,m_min = -10**10,0
p_count,p_min_idx,p_max_idx = 0,0,0
m_count,m_min_idx,m_max_idx = 0,0,0
for a in A:
    if a < 0:
        if m_min > a:
            m_min = a
            m_min_idx = m_count
        if m_max < a:
            m_max = a
            m_max_idx = m_count
        m_total += a
        m.append(a)
        m_count += 1
    else:
        if p_min > a:
            p_min = a
            p_min_idx = p_count
        if p_max < a:
            p_max = a
            p_max_idx = p_count
        p_total += a
        p.append(a)
        p_count += 1

if len(m) == 0:
    print(p_total-2*p_min)
    for i in range(len(p)-1):
        if i != p_min_idx:
            print(p[p_min_idx],p[i])
            p[p_min_idx] -= p[i]
    print(p[-1],p[p_min_idx])

elif len(p) == 0:
    print(2*m_max-m_total)
    for i in range(len(m)-1):
        if i != m_max_idx:
            print(m[m_max_idx],m[i])
            m[m_max_idx] -= m[i]
    print(m[m_max_idx],m[-1])

else:
    print(p_total-m_total)
    for i,v in enumerate(p):
        if i != p_max_idx:
            print(m[0], v)
            m[0] -= v
    for i in range(len(m)):
        print(p[p_max_idx],m[i])
        p[p_max_idx] -= m[i]