mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N, A, B, C = map(int, input().split())
    L = []
    for _ in range(N):
        L.append(int(input()))

    ans = 10**9
    for i in range(4 ** N):
        AA = []
        BB = []
        CC = []
        ii = i
        for j in range(N):
            k = ii % 4
            if k == 0:
                AA.append(L[j])
            elif k == 1:
                BB.append(L[j])
            elif k == 2:
                CC.append(L[j])
            ii >>= 2
        if len(AA) * len(BB) * len(CC) == 0:
            continue
        ans_new = abs(sum(AA) - A) + 10*(len(AA)-1) + abs(sum(BB) - B) + 10*(len(BB)-1) + abs(sum(CC) - C) + 10*(len(CC)-1)
        ans = min(ans, ans_new)
    print(ans)


if __name__ == '__main__':
    main()
