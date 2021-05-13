def main():
    N = int(input())
    any = 0
    A = map(int, input().split())
    colors = set([])
    for a in A:
        if 1 <= a <= 399:
            colors.add('gray')
        elif 400 <= a <= 799:
            colors.add('brown')
        elif 800 <= a <= 1199:
            colors.add('green')
        elif 1200 <= a <= 1599:
            colors.add('light blue')
        elif 1600 <= a <= 1999:
            colors.add('blue')
        elif 2000 <= a <= 2399:
            colors.add('yellow')
        elif 2400 <= a <= 2799:
            colors.add('orange')
        elif 2800 <= a <= 3199:
            colors.add('red')
        else:
            any += 1

    if any == 0:
        print(len(colors), len(colors))
    elif len(colors) == 0:
        print(1, any)
    else:
        print(len(colors), len(colors) + any)


if __name__ == '__main__':
    main()
