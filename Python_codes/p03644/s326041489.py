# vim: fileencoding=utf-8


def main():
    n = int(input())
    ans = n
    max = 0
    for i in range(1, n + 1):
        c = len(bin(i)) - bin(i).rfind("1") - 1
        if max < c:
            max = c
            ans = i
    print(ans)


if __name__ == "__main__":
    main()
