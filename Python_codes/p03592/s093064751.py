n, m, k = map(int, input().split())

ans = False
for i in range(n + 1):
    if ans:
        break
    for j in range(m + 1):
        if i * (m - j) + (n - i) * j == k:
            ans = True
            break

if ans:
    print('Yes')
else:
    print('No')
