import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, *b = map(int, read().split())

a = [b[0]]
for i in range(1, n-1):
    a.append(min(b[i - 1], b[i]))
a.append(b[-1])
print(sum(a))
