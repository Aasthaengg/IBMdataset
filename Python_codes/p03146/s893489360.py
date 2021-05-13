def main():
    def fun(n):
        if n % 2 == 0:
            return int(n / 2)
        else:
            return 3 * n + 1

    s = int(input())
    vals = [s]
    while True:
        new_v = fun(vals[-1])
        if new_v in vals:
            print(len(vals) + 1)
            break
        else:
            vals.append(new_v)


if __name__ == '__main__':
    main()
