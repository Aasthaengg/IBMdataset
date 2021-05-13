N, K = map(int, input().split())

tmp = 0
for i in range(1, N + 1):
    if i%2 == 1:
        tmp += 1
        
if tmp >= K:
    print('YES')
else:
    print('NO')