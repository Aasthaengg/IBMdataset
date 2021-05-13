import sys

x = input()
d = {}
result = 0

for line in sys.stdin:
    n, = line.strip().split(" ")
    n = int(n)
    if n-1 in d:
        d[n] = d[n-1] + 1
    else:
        d[n] = 1
    result = max(d[n], result)

print(int(x) - result)
