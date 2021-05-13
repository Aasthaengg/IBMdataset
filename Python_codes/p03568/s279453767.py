def main():
    N = int(input())
    A = list(map(int,(input().split())))

    al = 3 ** N
    minus = 1
    for a in A:
        if a % 2 ==0:
            minus *= 2
    print(al-minus)


if __name__ == '__main__':
    main()
