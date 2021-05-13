import sys
readline = sys.stdin.buffer.readline

N = int(readline())
A = [[] for _ in range(N)]

for i in range(N):
    count = int(readline())
    for j in range(count):
        x, y = map(int, readline().split())
        x -= 1
        A[i].append([x, y])


ans = 0
for i in range(2**N):
    good = [0] * N
    f = 1
    for j in range(N):
        if (i >> j) & 1:
            good[j] = 1

    for k in range(N):
        if good[k]:
            for x, y in A[k]:
                if good[x] != y:
                    f = 0
    if f:
        ans = max(ans, sum(good))

print(ans)