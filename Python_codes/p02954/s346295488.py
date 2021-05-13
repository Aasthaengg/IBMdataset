def main():
    s = input()

    rs, ls = 0, 0
    prev = ''
    A = [0] * len(s)
    for ci, c in enumerate(s):
        if c == 'R':
            if prev == 'l':
                A[ci - ls - 1] = rs//2 + ls//2 if rs % 2 == 0 \
                    else rs//2 + 1 + ls//2
                A[ci - ls] = rs//2 + ls//2 if ls % 2 == 0 \
                    else rs//2 + ls//2 + 1
                rs, ls = 0, 0

            rs += 1
            prev = 'r'
        else:
            ls += 1
            prev = 'l'

    A[-ls - 1] = rs//2 + ls//2 if rs % 2 == 0 \
        else rs//2 + 1 + ls//2
    A[-ls] = rs//2 + ls//2 if ls % 2 == 0 \
        else rs//2 + ls//2 + 1

    print(' '.join([str(a) for a in A]))


if __name__ == '__main__':
    main()
