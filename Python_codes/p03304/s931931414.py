import sys
n, m, d = [int(i) for i in sys.stdin.readline().split()]
if d >= n:
    print(0)
elif d == 0:
    print(1 / n * (m - 1))
else:
    _mean = max(0, n - d*2) * 2 / n**2
    _mean += (d * 2 - max(0, d * 2 - n))/ n**2
    print(_mean * (m - 1))