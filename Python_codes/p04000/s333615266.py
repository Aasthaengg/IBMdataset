import sys
sys.stdin.readline

def main():
    H, W, N = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    X = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    Y = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    XY = list(zip(X, Y))
    S = {}
    for a, b in AB:
        for x, y in XY:
            k = (a+x, b+y)
            S.setdefault(k, 0)
            S[k] += 1
    ans = [0] * 10
    for (x, y), v in S.items():
        if 1 < x < H and 1 < y < W:
            ans[v] += 1
    ans[0] = (H-2)*(W-2)-sum(ans[1:])
    print(*ans, sep="\n")

if __name__ == "__main__":
    main()