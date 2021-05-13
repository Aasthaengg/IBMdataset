MOD = 1000000007

pattern = [0] * 10
pattern[0] = 1
pattern[1] = 1
for i in range(2, 8 + 1):
    pattern[i] = pattern[i-1] + pattern[i-2]


def single_down(idx_from, idx_to, W):
    if idx_from == idx_to:
        return pattern[idx_from - 1] * pattern[W - idx_from]
    else:
        left = min(idx_from, idx_to) - 1
        right = W - max(idx_from, idx_to)
        return pattern[left] * pattern[right]


def main():
    H, W, K = map(int, input().split())

    ptn = [[0] * W]
    ptn[0][0] = 1
    for h in range(1, H + 1):
        ptn.append([])
        ptn[h] = [0] * W
        for w in range(0, W):
            ptn[h][w] = ptn[h-1][w] * single_down(w+1, w+1, W) % MOD
            if w > 0:
                ptn[h][w] += ptn[h-1][w-1] * single_down(w, w+1, W) % MOD
            if w < W-1:
                ptn[h][w] += ptn[h-1][w+1] * single_down(w+2, w+1, W) % MOD
            ptn[h][w] %= MOD

    print(ptn[H][K-1])


if __name__ == '__main__':
    main()
