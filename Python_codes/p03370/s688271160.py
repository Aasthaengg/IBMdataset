import sys

input = sys.stdin.readline


def main():
    N, X = map(int, input().split())
    m = [None] * N
    for i in range(N):
        m[i] = int(input())

    min_m = min(m)
    X -= sum(m)
    ans = N + X // min_m

    print(ans)


if __name__ == "__main__":
    main()
