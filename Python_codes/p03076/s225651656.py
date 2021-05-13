import sys
input = sys.stdin.read

A = list(map(int, input().split()))

res = 0
mi = 10

for a in A:
    x, y = divmod(a, 10)
    if not y:
        res += x
    else:
        res += x + 1
        mi = min(mi, y)
print(res * 10 + mi - 10)
