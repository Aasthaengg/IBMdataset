def input_from_console():
    n, k = map(int, input().split())

    return n, k


def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def main():
    n, k = input_from_console()
    print(n-k+1)



if __name__ == "__main__":
    main()
