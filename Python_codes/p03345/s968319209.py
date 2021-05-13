def main():
    a, b, c, k = map(int, input().split())

    f = k % 2 == 0
    ans = (b - a) * (-1) ** f
    print(ans if abs(ans) < 10 ** 18 else 'Unfair')


if __name__ == '__main__':
    main()
