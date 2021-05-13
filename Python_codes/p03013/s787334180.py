N, M = map(int, input().split())

if N == 1:
    print(1)
else:
    s = [-1] * N
    s[0] = 1
    s[1] = 1

    for m in range(0, M):
        i = int(input())
        s[i] = 0

    for n in range(2, N):
        if s[n] == 0:
            continue
        s[n] = s[n - 1] + s[n - 2]

    print((s[N-1] + s[N-2]) % 1000000007)
