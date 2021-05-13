n, m, k = map(int, input().split())

ans = set()

for i in range(m+1):
    cnt = i * n
    rev = m - i
    for j in range(n+1):
        ans.add(cnt + (rev - i) * j)

if k in ans:
    print('Yes')
else:
    print('No')
