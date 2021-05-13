from collections import Counter

n = int(input())
A = list(map(int, input().split()))
D = Counter(A)
res = []
for k, v in D.items():
    if v >= 2:
        for _ in range(v // 2):
            res.append(k)

if len(res) < 2:
    print(0)
else:
    res = sorted(res, reverse=True)
    print(res[0] * res[1])
