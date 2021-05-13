import itertools

n, k = list(map(int, input().split()))
ab = [[] for _ in range(n)]
for i in range(n):
    ab[i] = list(map(int, input().split()))
ab.sort(key=lambda x: x[0])
az, bz = list(zip(*ab))

accb = list(itertools.accumulate(bz))
idx = 0
for j, v in enumerate(accb):
    if k <= v:
        idx = j
        break
print(az[idx])
