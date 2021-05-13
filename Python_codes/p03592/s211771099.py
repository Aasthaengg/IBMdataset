N, M, K = map(int, input().split())

success = False
for x in range(M + 1):
    for y in range(N + 1):
        temp = (M - x) * y + (N - y) * x
        if temp == K:
            success = True

if success:
    print('Yes')
else:
    print('No')