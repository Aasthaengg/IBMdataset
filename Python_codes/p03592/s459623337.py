N, M, K = map(int, input().split())
ok = False
for i in range(N + 1):
    for j in range(M + 1):
        num = (i * M) + (j * N) - i * j * 2
        if num == K:
            ok = True
if ok:
    print('Yes')
else:
    print('No')
