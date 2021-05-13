import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = [0] * N
    for i in range(N):
        A[i] = int(input())

    ans = "first" if any(a % 2 == 1 for a in A) else "second"
    print(ans)


if __name__ == "__main__":
    main()
