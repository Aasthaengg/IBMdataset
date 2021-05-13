def main():
    N = int(input())
    ary = [2 ** n for n in range(7, 0, -1)]

    for i, a in enumerate(ary):
        if N < a:
            continue
        else:
            print(a)
            return
    print(N)


main()
