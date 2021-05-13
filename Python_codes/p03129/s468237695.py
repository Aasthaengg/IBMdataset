n, k = map(int, input().split())

x = [i for i in range(1, n+1)][::2]

if len(x) >= k:
    print('YES')
else:
    print('NO')