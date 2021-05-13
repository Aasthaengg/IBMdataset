mod = 1000000007
eps = 10**-9
inf = 10**15


def main():
    import sys
    from bisect import bisect_left
    input = sys.stdin.buffer.readline

    A, B, Q = map(int, input().split())
    S = [-inf]
    for _ in range(A):
        S.append(int(input()))
    S.append(inf)
    T = [-inf]
    for _ in range(B):
        T.append(int(input()))
    T.append(inf)

    for _ in range(Q):
        x = int(input())
        i = bisect_left(S, x)
        j = bisect_left(T, x)
        ans = []
        ans.append(x - S[i-1] + abs(S[i-1] - T[j-1]))
        ans.append(x - S[i-1] + abs(S[i-1] - T[j]))
        ans.append(x - T[j-1] + abs(T[j-1] - S[i-1]))
        ans.append(x - T[j-1] + abs(T[j-1] - S[i]))
        ans.append(S[i] - x + abs(S[i] - T[j-1]))
        ans.append(S[i] - x + abs(S[i] - T[j]))
        ans.append(T[j] - x + abs(T[j] - S[i-1]))
        ans.append(T[j] - x + abs(T[j] - S[i]))
        print(min(ans))


if __name__ == '__main__':
    main()
