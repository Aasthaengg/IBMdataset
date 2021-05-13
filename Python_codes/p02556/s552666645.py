N = int(input())
A = [[int(a) for a in input().split()] for _ in range(N)]
for i in range(N):
    z = A[i][0] + A[i][1]
    w = A[i][0] - A[i][1]
    if i==0:
        M_z = m_z = z
        M_w = m_w = w
    if z > M_z: M_z = z
    if z < m_z: m_z = z
    if w > M_w: M_w = w
    if w < m_w: m_w = w
print(max(M_z-m_z,M_w-m_w))