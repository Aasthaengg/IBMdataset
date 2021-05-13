
H, W, K = map(int, input().split())
X = [list(input()) for _ in range(H)]
MOD = 10 ** 9 + 7
ans = MOD

for bit in range(2 ** (H - 1)):
    n = bin(bit).count("1")
    ctr = [0] * (n + 1)  # Accumulation
    res = 0
    for j in range(W):
        k = 0
        tmp = [0] * (n + 1)  # One column
        for i in range(H):
            tmp[k] += int(X[i][j])
            if bit >> i & 1:
                k += 1

        # Check counts
        if any(v > K for v in tmp):
            res = MOD
            break
        elif any(u + v > K for u, v in zip(ctr, tmp)):
            # Split
            res += 1
            ctr = tmp[:]
        else:
            # Accumulate
            for i in range(n + 1):
                ctr[i] += tmp[i]

    ans = min(ans, res + n)

print(ans)
