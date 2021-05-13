n, m, k = map(int, input().split())

ans = 'No'
for n_ in range(n+1):
    for m_ in range(m+1):
        if n_*(m-m_) + m_*(n-n_) == k:
            ans = 'Yes'

print(ans)
