def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    P = []
    M = []
    for _ in range(N):
        x, y = map(int, input().split())
        P.append(x + y)
        M.append(x - y)
    P.sort()
    M.sort()
    ans = max(P[-1] - P[0], M[-1] - M[0])
    print(ans)


if __name__ == '__main__':
    main()
