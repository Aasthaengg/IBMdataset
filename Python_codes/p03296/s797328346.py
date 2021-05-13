import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = tuple(map(int, input().split()))

    ans = 0
    b = -1
    cnt = 0
    for a in A:
        if b == a:
            cnt += 1
        else:
            ans += cnt // 2
            cnt = 1
            b = a
    ans += cnt // 2

    print(ans)


if __name__ == "__main__":
    main()
