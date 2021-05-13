from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

ctr = defaultdict(int)

for i in range(N):
    tmp = [0] * 26
    for j in range(10):
        tmp[ord(S[i][j]) - ord("a")] += 1
    ctr[tuple(tmp)] += 1

ans = 0
for v in ctr.values():
    ans += v * (v - 1) // 2
print(ans)
