n, m = map(int, input().split())
cnt = {i: 0 for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1

if all(cnt[i] % 2 == 0 for i in range(1, n+1)):
    print('YES')
else:
    print('NO')