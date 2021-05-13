import sys

input = sys.stdin.readline


def main():
    N = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))

    ans = 0
    for i in range(N):
        if i == a[a[i]]:
            ans += 1
    ans //= 2

    print(ans)


if __name__ == "__main__":
    main()
