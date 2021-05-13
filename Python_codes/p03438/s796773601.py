import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
cnt = 0
for i in range(n):
    cnt += max(0, (b[i] - a[i] + 1) // 2)
if sum(b) - sum(a) >= cnt:
    print('Yes')
else:
    print('No')
