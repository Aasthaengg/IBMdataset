N,K = map(int,input().split())
l = [int(x) for x in input().split()]
ans = 0
for _ in range(K):
    m = max(l)
    ans += m
    m_i = l.index(m)
    l[m_i]=0

print(ans)
