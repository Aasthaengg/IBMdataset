# vim: fileencoding=utf-8


def main():
    n = int(input())
    li = []
    for i in range(n):
        li.append(int(input()))
    li.sort(reverse=True)
    ans = 1
    for i in range(1, n):
        if li[i - 1] > li[i]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
