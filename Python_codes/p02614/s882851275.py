import itertools

def main():
    H, W, K = map(int, input().split())
    C = [list(input().rstrip()) for _ in range(H)]
    ans = 0
    for h in itertools.product([0, 1], repeat=H):
        for w in itertools.product([0, 1], repeat=W):
            black = 0
            for r in range(H):
                for c in range(W):
                    if h[r] == 0 and w[c] == 0 and C[r][c] == "#":
                        black += 1
            if black == K:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
