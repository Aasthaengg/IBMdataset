def main():
    S = int(input())
    y3 = (S+10**9-1)//10**9
    x3 = 10**9 * y3 - S
    print(0, 0, 10**9, 1, x3, y3)


if __name__ == '__main__':
    main()
