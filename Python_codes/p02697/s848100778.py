N, M = map(int, input().split())

if N % 2 == 1:
    for i in range(M):
        j = N - i
        print(f'{i + 1} {j}')
else:
    for i in range(M):
        j = N - i
        if i < M / 2:
            print(f'{i + 1} {j}')
        else:
            print(f'{i + 1} {j - 1}')
