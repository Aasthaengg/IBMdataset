
N, M = map(int, input().split())

if M % N == 0:
    print(M // N)
else:
    ans = 1
    for n in range(1, M // N + 1):
        res = M - n * N
        if res % n == 0:
            ans = n

    print(ans)
