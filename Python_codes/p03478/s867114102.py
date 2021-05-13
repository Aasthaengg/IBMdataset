# vim: fileencoding=utf-8


def main():
    n, a, b = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        s = str(i)
        c = 0
        for j in range(len(s)):
            c += int(s[j])
        if c >= a and c <= b:
            ans += i
    print(ans)


if __name__ == "__main__":
    main()
