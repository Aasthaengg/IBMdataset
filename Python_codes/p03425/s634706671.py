import itertools

N = int(input())
S = [input() for _ in range(N)]

cnt = [0 for _ in range(5)]
for s in S:
    if s[0] == "M":
        cnt[0] += 1
    elif s[0] == "A":
        cnt[1] += 1
    elif s[0] == "R":
        cnt[2] += 1
    elif s[0] == "C":
        cnt[3] += 1
    elif s[0] == "H":
        cnt[4] += 1

ans = 0
for i, j, k in itertools.combinations(cnt, r=3):
    ans += i * j * k

print(ans)
