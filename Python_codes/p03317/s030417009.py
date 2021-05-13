N,K = map(int, input().split())
A = [int(i) for i in input().split()]

if N == K:
    print(1)
else:
    cnt = 1
    N -= K
    while N > 0:
        cnt += 1
        N -= K
        N += 1
    print(cnt)