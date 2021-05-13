def main():
    n = int(input())
    A = input().split()
    evens = []
    odds = []
    for idx, a in enumerate(A, start=1):
        if idx % 2 == 0:
            evens.append(a)
        else:
            odds.append(a)

    if n % 2 == 0:
        evens.reverse()
        print((' ').join(evens + odds))
    else:
        odds.reverse()
        print((' ').join(odds + evens))


if __name__ == '__main__':
    main()
