def main():
    nm = [int(_x) for _x in input().split()]
    n = nm[0]
    m = nm[1]
    a = [int(_x) for _x in input().split()]
    result = n - sum(a)
    if result < 0:
        print(-1)
    else:
        print(result)


main()
