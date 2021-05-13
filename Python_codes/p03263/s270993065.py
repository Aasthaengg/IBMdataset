# coding: utf-8

# https://atcoder.jp/contests/abc109
# -18:59 done


def main():
    H, W = map(int, input().split())
    a = [None] * H
    for i in range(H):
        a[i] = list(map(int, input().split()))

    operates = []
    for i in range(H):
        for j in range(W-1):
            if a[i][j] % 2 == 1:
                a[i][j] -= 1
                a[i][j+1] += 1
                operates.append("{} {} {} {}".format(i+1, j+1, i+1, j+2))
        if i < H-1 and a[i][-1] % 2 == 1:
            a[i][-1] -= 1
            a[i+1][-1] += 1
            operates.append("{} {} {} {}".format(i+1, W, i+2, W))

    N = len(operates)
    print(N)
    for i in range(N):
        print(operates[i])


main()
# print(main())
