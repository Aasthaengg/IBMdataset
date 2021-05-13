# vim: fileencoding=utf-8


def main():
    n, k = map(int, input().split())
    li = [0] * n
    a = list(map(int, input().split()))
    for i in a:
        li[i - 1] += 1

    li.sort(reverse=True)
    print(sum(li[k:]))


if __name__ == "__main__":
    main()
