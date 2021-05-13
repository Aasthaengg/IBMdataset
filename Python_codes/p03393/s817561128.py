def main():
    from collections import Counter
    from string import ascii_lowercase

    S = input()

    ctr = Counter(S)
    for count in ctr.values():
        if count > 1:
            print(-1)
            return

    for char in ascii_lowercase:
        if ctr[char] == 0:
            print(S + char)
            return

    lis = list(S)
    stock = []
    ma = None
    while lis:
        x = lis.pop()
        if ma is None or ma < x:
            ma = x
        stock.append(x)
        if lis and lis[-1] < ma:
            stock.sort()
            for char in stock:
                if lis[-1] < char:
                    print(''.join(lis[:-1]) + char)
                    return
    print(-1)


if __name__ == '__main__':
    main()
