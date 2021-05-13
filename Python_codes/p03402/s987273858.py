a, b = map(int, input().split())
k = 50
ans = []
for _ in range(k):
    ans += [['#'] * (2 * k)]
for _ in range(k):
    ans += [['.'] * (2 * k)]

for i in range(a - 1):
    ans[(i // k) * 2][(i % k) * 2] = '.'
for i in range(b - 1):
    ans[(i // k) * 2 + k + 1][(i % k) * 2] = '#'

print('{} {}'.format(2*k, 2*k))
for i in range(2 * k):
    for j in range(2 * k):
        print(ans[i][j], end='')
    print()