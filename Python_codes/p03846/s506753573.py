from itertools import groupby


def main():
    n = int(input())
    xs = sorted(list(map(int, input().split())))

    if n == 1:
        if xs[0] == 0:
            print(1)
        else:
            print(0)
        return

    xxs = [list(it) for k, it in groupby(xs)]

    if len([xs for xs in xxs if len(xs) != 2 and xs[0] != 0]) > 0:
        print(0)
        return

    ans = 1
    for i in range(n//2):
        ans *= 2
        ans %= 1000000007
    print(ans)


main()
