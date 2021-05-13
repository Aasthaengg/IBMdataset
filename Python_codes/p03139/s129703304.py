import sys
n, a, b = map(int ,sys.stdin.readline().strip().split())
mi = max(0, a+b-n)
ma = min(n, min(a, b))
print("{} {}".format(ma, mi))