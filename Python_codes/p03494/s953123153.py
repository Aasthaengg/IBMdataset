# vim: fileencoding=utf-8


def main():
    n = int(input())
    li = list(map(int, input().split()))
    c = 0
    end = False
    while True:
        for i in range(n):
            if li[i] % 2:
                end = True
                break
            li[i] = li[i] / 2
        if end:
            break
        else:
            c += 1
    print(c)


if __name__ == "__main__":
    main()
