# vim: fileencoding=utf-8


def main():
    n, x = map(int, input().split())
    min = 1001
    ans = n
    for i in range(n):
        m = int(input())
        x -= m
        if min > m:
            min = m
    ans += x // min
    print(ans)


if __name__ == "__main__":
    main()
