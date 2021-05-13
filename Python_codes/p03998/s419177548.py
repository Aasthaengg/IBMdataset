def main():
    a = input()
    b = input()
    c = input()

    i, j, k = 0, 0, 0

    temp = a[i]

    while True:

        if temp == 'a':
            if i == len(a):
                winner = 'A'
                break
            temp = a[i]
            i += 1
        elif temp == 'b':
            if j == len(b):
                winner = 'B'
                break
            temp = b[j]
            j += 1
        elif temp == 'c':
            if k == len(c):
                winner = 'C'
                break
            temp = c[k]
            k += 1

    print(winner)


if __name__ == '__main__':
    main()
