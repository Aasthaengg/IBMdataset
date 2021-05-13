def main():
    X = int(input())
    a_max = None
    a = 1
    while True:
        if a**5 - (a-1)**5 > X:
            a_max = a - 1
            break
        else:
            a += 1
    a_min = None
    a = -1
    while True:
        if a**5 - (a-1)**5 > X:
            a_min = a + 1
            break
        else:
            a -= 1

    for a in range(a_min, a_max+1):
        for b in range(a_min-1, a_max):
            if a**5 - b**5 == X:
                print(a, b)
                exit()


if __name__ == '__main__':
    main()
