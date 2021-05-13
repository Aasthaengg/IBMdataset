import sys

input = sys.stdin.readline


def main():
    N = int(input())

    ans = float("inf")
    for A in range(1, N):
        B = N - A
        total = sum(int(s) for s in str(A)) + sum(int(s) for s in str(B))
        if total < ans:
            ans = total

    print(ans)


if __name__ == "__main__":
    main()
