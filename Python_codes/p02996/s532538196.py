import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


n = int(readline())
ab = [list(map(int, readline().split())) for _ in range(n)]
ab.sort(key=lambda x: x[1])
cost = 0
for i in range(n):
    cost += ab[i][0]
    if cost > ab[i][1]:
        print('No')
        exit()
print('Yes')
