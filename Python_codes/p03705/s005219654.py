if __name__ == "__main__":
    n, a, b = map(int, input().split())

    if n == 1 and a == b:
        print(1)
        exit()
    elif n == 1:
        print(0)
        exit()
    elif a > b:
        print(0)
        exit()
    elif n == 2:
        print(1)
        exit()

    n_min = b + (n-1)*a
    n_max = a + (n-1)*b

    print(n_max-n_min+1)
