n, k, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(q)]
start = [k - q] * n

for i in range(q):
    start[a[i][0] - 1] += 1

for i in range(n):
    if start[i] > 0:
        print('Yes')
    else:
        print('No')