N = int(input())
a = list(map(int, input().split()))

MAX = max(a)
MIN = min(a)

if MIN < 0:
    print(2 * N - 1)
    if abs(MAX) >= abs(MIN):
        idx = a.index(MAX) + 1
        for i in range(1, N + 1):
            print(idx, i)
        for i in range(1, N):
            print(i, i + 1)
    else:
        idx = a.index(MIN) + 1
        for i in range(1, N + 1):
            print(idx, i)
        for i in range(N, 1, -1):
            print(i, i - 1)
else:
    print(N - 1)
    for i in range(1, N):
        print(i, i + 1)