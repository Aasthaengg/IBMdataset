import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, m = map(int, readline().split())
ipy = [[i] + list(map(int, readline().split())) for i in range(m)]

ipy.sort(key=lambda x: x[2])

c = [0] * n
l = []
for i, p, y in ipy:
    c[p - 1] += 1
    x = str(format(p, '06') + format(c[p - 1], '06'))
    l.append([i, x])

l.sort()
for i, v in l:
    print(v)