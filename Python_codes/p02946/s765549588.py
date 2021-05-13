def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    k, x = Input()
    return " ".join(map(str, list(range(x-(k-1), x+k))))


print(main())