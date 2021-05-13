def main():
    s = list(map(int, list(input())))

    c0 = 0
    c1 = 0

    for x in s:
        if x == 1:
            c1 += 1
        else:
            c0 += 1

    print(2*min(c0, c1))

if __name__ == '__main__':
    main()