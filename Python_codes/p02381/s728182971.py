import sys

while True:
    n = int(input())
    if n == 0:
        break
    s = [int(x) for x in sys.stdin.readline().split()]
    m = sum(s) / n
    a = (sum([(x - m) ** 2 for x in s]) / n) ** 0.5
    print(a)