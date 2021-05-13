N = int(input())
res = set([0])
for _ in range(N):
    s = int(input())
    res |= set([r + s for r in res])
res = list(res)
res.sort()
n = len(res)
for i in range(n-1, -1, -1):
    if res[i] % 10 == 0:
        continue
    print(res[i])
    break
else:
    print(0)