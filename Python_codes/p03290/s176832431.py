D, G = map(int, input().split())
P = [0] * D
C = [0] * D
ans = float("inf")

for i in range(D):
    P[i], C[i] = map(int, input().split())

for bit in range(1 << D):
    score = 0
    cnt = 0
    unused = set(range(1, D+1))
    for i in range(D):
        if (bit >> i) & 1 == 1:
            cnt += P[i]
            score += 100 * (i + 1) * P[i] + C[i]
            unused.discard(i + 1)

    if score < G:
        use = max(unused)
        num = min(P[use - 1], -(-(G - score) // (use * 100)))
        cnt += num
        score += use * 100 * num

    if score >= G:
        ans = min(ans, cnt)

print(ans)
