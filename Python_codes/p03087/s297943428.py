def main():
    from itertools import accumulate
    N, Q = (int(i) for i in input().split())
    S = [s for s in input()]
    A = [0]*N
    for i in range(1, N):
        if S[i-1] == "A" and S[i] == "C":
            A[i] += 1
    acc = list(accumulate([0] + A))

    for _ in range(Q):
        le, ri = (int(i) for i in input().split())
        ans = acc[ri] - acc[le-1]
        if 0 < le and S[le-2] == "A" and S[le-1] == "C":
            ans -= 1
        print(ans)


if __name__ == '__main__':
    main()
