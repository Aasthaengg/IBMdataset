def mapt(fn, *args):
    return list(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b = Input()
    if a >= 13:
        print(b)
    elif 6 <= a <= 12:
        print(b//2)
    else:
        print(0)

main()