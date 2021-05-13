import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    n = int(input().strip())
    A = [None] + [int(i) for i in input().strip().split()]
    ans = 0
    for i in range(1, n + 1):
        if i == A[A[i]]:
            ans += 1

    print(ans // 2)

    return


if __name__ == "__main__":
    main()