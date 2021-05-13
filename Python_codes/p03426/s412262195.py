def main():
    import sys
    input = sys.stdin.readline
    H, W, D = (int(i) for i in input().split())
    A = [[int(i) for i in input().split()] for j in range(H)]
    S = [0] * (H*W + 1)

    dic = [(-1, -1) for i in range(H*W + 1)]
    for h in range(H):
        for w in range(W):
            dic[A[h][w]] = (h+1, w+1)

    for idx in range(1, H*W+1):
        if H*W < idx+D:
            continue
        i, j = dic[idx]
        x, y = dic[idx + D]
        S[idx+D] = abs(x - i) + abs(y - j) + S[idx]

    Q = int(input())
    for query in range(Q):
        le, ri = (int(i) for i in input().split())
        print(S[ri] - S[le])


if __name__ == '__main__':
    main()
