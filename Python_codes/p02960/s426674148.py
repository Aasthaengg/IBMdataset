def main():
    MOD = 10 ** 9 + 7

    s = input()
    r = [0] * 13
    r[0] = 1
    p = 1
    for c in reversed(s):
        if c == '?':
            tank = []
            for x in range(10):
                x = x * p % 13
                tank.append(r[13 - x:] + r[:13 - x])
            r = map(sum, zip(*tank))
            *r, = map(lambda x: x % MOD, r)


        else:
            x = int(c)
            x = x * p % 13
            r = r[13 - x:] + r[:13 - x]
        p = p * 10 % 13

    print(r[5])


if __name__ == '__main__':
    main()
