from collections import Counter

n = 50
comb = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(n + 1):
        if j == 0 or j == i:
            comb[i][j] = 1
        else:
            comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]

N, A, B, *X = map(int, open(0).read().split())

ctr = Counter(X)
value = 0
cnt = 0
cand = []
for i, (k, v) in enumerate(sorted(ctr.items(), reverse=True)):
    if i == 0 and A <= v:
        value = k * v
        cnt = v
        cand.append((k, v))
        break

    # Add
    c = min(v, A - cnt)
    value += k * c
    cnt += c
    cand.append((k, c))
    if cnt == A:
        break

# Count combinations
ans = 1
if len(cand) == 1:
    _, n = cand[0]
    ans = 0
    for k in range(A, min(v, B) + 1):
        ans += comb[n][k]
else:
    ans = 1
    for k, c in cand:
        ans *= comb[ctr[k]][c]

print(value / cnt)
print(ans)
