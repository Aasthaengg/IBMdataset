from collections import defaultdict
A = input()
N = len(A)
d = defaultdict(int)
for a in A:
    d[a] += 1
cnt = 0
for k, v in d.items():
    cnt += v * (v - 1) // 2
ans = N * (N - 1) // 2 - cnt
print(ans + 1)
