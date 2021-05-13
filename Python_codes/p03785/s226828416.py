import sys

input = sys.stdin.readline


def main():
    N, C, K = map(int, input().split())
    T = [0] * N
    for i in range(N):
        T[i] = int(input())

    T.sort()
    ans = 0
    s = 0  # Time when the bus comes
    m = 0  # Current numbers of passengers
    for t in T:
        if m == 0:
            s = t
            m = 1
            ans += 1
        else:
            if t <= s + K:
                m += 1
            else:
                s = t
                m = 1
                ans += 1
        if m == C:
            m = 0

    print(ans)


if __name__ == "__main__":
    main()
