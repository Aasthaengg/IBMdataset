from collections import defaultdict
A = input()
N = len(A)

d = defaultdict(list)
for i, a in enumerate(A):
    d[a].append(i)

pair = 0
for k, v in d.items():
    n = len(v)
    pair += n * (n - 1) // 2

ans = N * (N - 1) // 2
ans = ans - pair + 1
print(ans)
