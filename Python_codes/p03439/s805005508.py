import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    def query(x):
        print(x)
        ret = input()
        if ret == "Vacant":
            sys.exit()
        return ret

    n = int(readline())

    l = 0
    r = n - 1

    op = {"Male": "Female", "Female": "Male"}

    ls = query(l)
    rs = query(r)

    while r - l > 1:
        mid = (l + r) // 2
        ms = query(mid)
        if (mid - l) % 2 == 0:
            if ls == ms:
                l = mid + 1
                ls = op[ms]
            else:
                r = mid - 1
                rs = op[ms]
        else:
            if ls == ms:
                r = mid - 1
                rs = op[ms]
            else:
                l = mid + 1
                ls = op[ms]
    query(l)
    query(r)


if __name__ == '__main__':
    main()
