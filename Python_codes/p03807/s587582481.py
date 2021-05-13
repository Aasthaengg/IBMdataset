import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    n_odd = 0
    for a in A:
        n_odd += 1 if a % 2 == 1 else 0

    if n_odd % 2 == 0:
        ans = "YES"
    else:
        ans = "NO"
    print(ans)


if __name__ == "__main__":
    main()
