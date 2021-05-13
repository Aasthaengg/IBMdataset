def main():
    N = int(input())

    if N is 0:
        print(0)
        return

    ans = []  # 末尾の桁から
    while N:
        q, r = divmod(N, 2)
        ans.append(r)
        N = -q
    print(*reversed(ans), sep='')


if __name__ == '__main__':
    main()
