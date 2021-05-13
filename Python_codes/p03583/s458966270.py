def main():
    n = int(input())
    x, y, z = 0, 0, 0
    f = False
    for i in range(1, 3501):
        for j in range(i, 3501):
            if (4*i*j - i*n - j*n) > 0 and i*j*n % (4*i*j - i*n - j*n) == 0:
                x = i
                y = j
                z = i*j*n // (4*i*j - i*n - j*n)
                f = True
                break
        if f:
            break
    print(x, y, z)

if __name__ == "__main__":
    main()
