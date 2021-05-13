n, m, k = map(int, input().split())
set_num = set([])
for n_i in range(n + 1):
    for m_i in range(m + 1):
        set_num.add((n_i * m) + (m_i * n) - ((n_i * m_i) * 2))
if k in set_num:
    print("Yes")
else:
    print("No")