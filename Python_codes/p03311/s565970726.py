import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = list(map(int, readline().split()))
a = sorted(x - i for i, x in enumerate(a))
low = (len(a) + 1) // 2 - 1
high = len(a) // 2
print(sum(a[high:]) - sum(a[:low + 1]))
