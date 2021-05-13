# vim: fileencoding=utf-8


def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort(reverse=True)
    ans = 0
    for i in range(n):
        ans += li[i * 2 + 1]
    print(ans)


if __name__ == "__main__":
    main()
