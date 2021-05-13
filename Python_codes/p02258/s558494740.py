import itertools
n = int(input())
R = [int(input()) for _ in range(n)]
ret = -(10 ** 9)
mn = R[0]
for r in itertools.islice(R, 1, len(R)):
    ret = max(ret, r - mn)
    mn = min(mn, r)
print(ret)