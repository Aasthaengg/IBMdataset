import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, *a = map(int, read().split())

l = [0,*a,0]


s = 0
for i in range(1, n + 2):
    s += abs(l[i] - l[i - 1])

for i in range(1, n + 1):
    delcost = abs(l[i + 1] - l[i]) + abs(l[i] - l[i - 1])
    addcost = abs(l[i + 1] - l[i - 1])
    print(s - delcost + addcost)