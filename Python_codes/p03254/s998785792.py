import sys

input = sys.stdin.readline


def main():
    N, x = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    ans = 0
    for i in range(N):
        if a[i] <= x:
            x -= a[i]
            ans += 1
        else:
            break

    if ans == N and x > 0:
        ans -= 1

    print(ans)


if __name__ == "__main__":
    main()
