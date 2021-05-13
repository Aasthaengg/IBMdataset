
N, K = map(int, input().split())

cnt = 0
for n in range(1, N + 1):
    tmp = 0
    while n < K:
        n *= 2
        tmp += 1
    cnt += 1 / 2 ** tmp

print(cnt / N)
