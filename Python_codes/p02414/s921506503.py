n, m, l = map(int, raw_input().split())

A, B = [], []
for ni in range(n):
    A.append(map(int, raw_input().split()))

for mi in range(m):
    B.append(map(int, raw_input().split()))

_B = list(map(list, zip(*B)))

for a in A:
    ret = []
    for b in _B:
        calc_result = 0
        for i, j in zip(a, b):
            calc_result += i*j
        ret += [calc_result]
    print "%s" % ' '.join(map(str, ret))