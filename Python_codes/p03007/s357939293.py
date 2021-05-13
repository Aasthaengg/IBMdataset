# diverta2019-2C - Successive Subtraction
def main():
    n = int(input())
    lst = sorted(map(int, input().rstrip().split()))
    s = lst[0]  # start
    l = lst[-1]  # last
    log = []
    for i in lst[1:-1]:
        if i > 0:
            log += [(s, i)]
            s -= i
        else:
            log += [(l, i)]
            l -= i
    log += [(l, s)]
    print(l - s)
    for i, j in log:
        print(i, j)


if __name__ == "__main__":
    main()