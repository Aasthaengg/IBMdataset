# coding: utf-8

def main():
    a, b, c = map(int, input().split())
    ans = 0

    if a == b and b == c and a % 2 == 0:
        ans = -1
    else:
        while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
            d = b / 2 + c / 2
            e = c / 2 + a / 2
            f = a / 2 + b / 2
            a, b, c = d, e, f
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
