def main():
    S = int(input())
    x1, y1 = 0, 0
    if S < 10**18:
        x2, y2 = 10**9, 1
        y3 = S // x2 + 1
        x3 = x2 * y3 - S
    else:
        x2, y2 = 10**9, 0
        x3, y3 = 0, 10**9
    print(' '.join(map(str, [x1, y1, x2, y2, x3, y3])))


if __name__ == '__main__':
    main()
