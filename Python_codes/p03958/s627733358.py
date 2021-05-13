import sys

readline = sys.stdin.buffer.readline

K, T = map(int, readline().split())
A = sorted(list(map(int, readline().split())))[::-1]

B = [-1 for _ in range(K)]

j = 0
for i, a in enumerate(A):
    for _ in range(a):
        if j <= K // 2 - 1:
            B[2 * j] = i
        else:
            B[2 * (j - K // 2) - 1] = i
        j += 1

cnt = 0
for i in range(1, K):
    if B[i - 1] == B[i]:
        cnt += 1

print(cnt)
