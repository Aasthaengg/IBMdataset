def main():
    X = int(input())
    k = 1
    while k*X % 360 != 0:
        k += 1
    print(k)


if __name__ == '__main__':
    main()
