from collections import Counter
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
a = list(map(int, readline().split()))
q = int(readline())

c = Counter(a)
l = [0]*(10 ** 5 + 1)
for k, v in c.items():
    l[k] = v

sm = sum(a)

for i in range(q):
    b, c = map(int, readline().split())
    sm += ((c-b) * l[b])
    print(sm)
    l[c] += l[b]
    l[b] = 0