#!python3

LI = lambda: list(map(int, input().split()))

# input
N, M = LI()
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]


def solve():
    n = N - M + 1
    b = "".join(B)
    for i in range(n):
        for j in range(n):
            a = ""
            for k in range(M):
                a += A[i + k][j : j + M]
            if a == b:
                return "Yes"
    return "No"


def main():
    ans = solve()
    print(ans)


if __name__ == "__main__":
    main()
