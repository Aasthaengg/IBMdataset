# vim: fileencoding=utf-8


def main():
    n = int(input())
    li = [0] * 102
    for i in range(n):
        d = int(input())
        li[d] = 1
    ans = 0
    for i in range(102):
        if li[i] == 1:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
