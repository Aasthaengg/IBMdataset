from collections import defaultdict
N, M = map(int, input().split())
dict = defaultdict(int)
for _ in range(N):
    line = list(map(int, input().split()))
    K = line[0]
    A = line[1:]
    for a in A:
        dict[a] += 1
ans = 0
for k, v in dict.items():
    if v == N:
        ans += 1
print(ans)
