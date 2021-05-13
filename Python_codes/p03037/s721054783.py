def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n, m = Input()
    max_l = 0
    min_r = 1e6
    for i in range(m):
        l, r = Input()
        max_l = max(max_l, l)
        min_r = min(min_r, r)

    ans = min_r - max_l + 1
    ans = max(ans, 0)
    print(ans)

main()