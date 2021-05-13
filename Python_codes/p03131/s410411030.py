import sys
k, a, b = [int(i) for i in sys.stdin.readline().split()]
if b - a <= 2:
    print(k + 1)
else:
    cnt = 0
    cnt += min(k, a - 1)
    bisk = 1 + cnt + (b - a) * ((k - cnt) // 2)
    bisk += (k - cnt) % 2
    print(bisk)