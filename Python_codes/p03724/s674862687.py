import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
ab = [list(map(int, readline().split())) for i in range(m)]
ans = [0] * n
for a, b in ab:
    ans[a - 1] += 1
    ans[b - 1] += 1
for i in range(n):
    if ans[i] % 2 == 1:
        print('NO')
        exit()
print('YES')
