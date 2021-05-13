def main():
    S = int(input())
    x1, y1 = 10**9, 1
    if S < 10**9:
        x1 = 1
        x2 = 0
        y2 = S
    else:
        y2 = 0--S//10**9
        x2 = x1*y2 - S
    print(0, 0, x1, y1, x2, y2)


if __name__ == '__main__':
    main()
