def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b = Input()
    if a % 2 !=  b % 2:
        print("IMPOSSIBLE")
    else:
        print((a+b)//2)

main()