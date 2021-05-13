def main():
    n, a, b = [int(i) for i in input().split()]

    if a + b == 0:
        print(0)
    else:
        c, r = n // (a + b), n % (a + b)
        nblue = c * a + min(a, r)
        print(nblue)

main()
