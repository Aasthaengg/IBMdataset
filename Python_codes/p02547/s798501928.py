N = int(input())
a = []
for _ in range(0, N):
    a1, a2 = map(int, input().split())
    a.append(a1)
    a.append(a2)
ans = ''
for i in range(0, (2 * N) - 1, 2):
    if a[i] == a[i + 1]:
        ans += 'Y'
    else:
        ans += 'N'

if 'YYY' in ans:
    print('Yes')
else:
    print('No')