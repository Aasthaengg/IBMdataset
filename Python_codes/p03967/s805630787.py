import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

S = list(input().strip())

m = {
    "g": 0,
    "p": 0,
}

for v in S:
    m[v] += 1

ans = -10 ** 18
p = len(S)
for g in range(p + 1):
    if g >= p - g:
        ans = max(ans, m["g"] - g)

print(ans)