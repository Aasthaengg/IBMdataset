from collections import Counter

n = int(input())
S = [''.join(sorted(input())) for _ in range(n)]
S_c = Counter(S)

ans = 0
for i in list(S_c.values()):
    ans += i * (i - 1) // 2

print(ans)