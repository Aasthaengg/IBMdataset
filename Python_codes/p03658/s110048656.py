# vim: fileencoding=utf-8


def main():
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort(reverse=True)
    print(sum(li[:k]))


if __name__ == "__main__":
    main()
