def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b, c = Input()
    x = a - b
    use = min(c, x)
    ans = c -use
    print(ans)


main()