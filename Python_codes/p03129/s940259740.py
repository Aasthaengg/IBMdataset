N, K = map(int, input().split())

for i in range(1, N+1, 2):
    K -= 1

if K > 0:
    print('NO')
else:
    print('YES')
