def main():
    s = int(input())
    # a, b, c = map(int, input().split())
    # h = list(map(int, input().split()))
    # s = input()

    amount = [s]
    i = 1
    while True:
        if s % 2 == 0:
            s = s // 2
        else:
            s = 3*s + 1
        i += 1
        if s in amount:
            print(i)
            break
        amount.append(s)


if __name__ == '__main__':
    main()
