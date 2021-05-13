mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.buffer.readline

    N, C, K = map(int, input().split())
    T = []
    for _ in range(N):
        T.append(int(input()))
    T.sort()

    if C == 1:
        print(N)
        exit()

    cnt = 0
    ans = 0
    t0 = -10**10
    for t in T:
        if t0 + K < t:
            t0 = t
            cnt = 1
            ans += 1
        else:
            cnt += 1
            if cnt == C:
                cnt = 0
                t0 = -10**10
    print(ans)


if __name__ == '__main__':
    main()
