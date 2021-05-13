def q_c():
    a, b = map(int, input().split())

    if a > b:
        tmp = a
        a = b
        b = tmp

    b0 = b
    a0 = a
    while b % a != 0:
        c = b % a
        b = a
        a = c

    print(int(b0 * a0 / a))


if __name__ == '__main__':
    q_c()
