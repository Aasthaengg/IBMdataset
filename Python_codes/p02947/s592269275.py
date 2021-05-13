import sys

input = sys.stdin.readline
D = {}
for _ in range(int(input())):
    d = {}
    for s in sorted(input().rstrip()):
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    ds = "".join((k + str(v)) for k, v in d.items())
    if ds in D:
        D[ds] += 1
    else:
        D[ds] = 1

print(sum((v * (v - 1)) // 2 for v in D.values()))

