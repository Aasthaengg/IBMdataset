# vim: fileencoding=utf-8


def main():
    n = int(input())
    ans = float("inf")
    for i in range(2, n // 2 + 2):
        a = i
        b = n - a
        na = sum(map(int, list(str(a))))
        nb = sum(map(int, list(str(b))))
        if ans > na + nb:
            ans = na + nb
    print(ans)


if __name__ == "__main__":
    main()
