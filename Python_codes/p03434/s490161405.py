# vim: fileencoding=utf-8


def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort(reverse=True)
    a = sum(li[::2])
    b = sum(li[1::2])
    ans = a - b
    print(ans)


if __name__ == "__main__":
    main()
