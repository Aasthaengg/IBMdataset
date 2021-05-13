N,M = [int(i) for i in input().split()]
count = 0
if 2 * N <= M:
    count = N + (M - 2 * N) // 4
else:
    count = M // 2

print(count)
