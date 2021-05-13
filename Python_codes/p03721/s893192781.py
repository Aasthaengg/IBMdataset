import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, k = map(int, readline().split())
ab = [list(map(int, readline().split())) for _ in range(n)]

ab.sort()

cnt = 0
for i in range(n):
    cnt += ab[i][1]
    if cnt >= k:
        print(ab[i][0])
        exit()
