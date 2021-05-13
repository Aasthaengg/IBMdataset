
def check_use_count(X, Y):
    a = (2 * X - Y) // 3
    b = X - 2 * a

    return a, b


def factorial(x, mod):
    if x == 0:
        return 1

    x %= mod

    for i in range(x-1, 0, -1):
        x *= i
        x %= mod

    return x


def main():
    mod = 10**9 + 7
    X, Y = [int(x) for x in input().split()]

    # 必ず3で割り切れる
    if (X + Y) % 3 != 0:
        print(0)
        exit()

    a, b = check_use_count(X, Y)

    # 0だったら行けない
    if a < 0 or b < 0:
        print(0)
        exit()

    # 移動パターンの計算
    # !(a + b) / !a * !b
    up = factorial(a + b, mod)
    fact_a = factorial(a, mod)
    fact_b = factorial(b, mod)

    down = fact_a * fact_b % mod

    result = up * pow(down, mod - 2, mod) % mod
    print(result)


if __name__ == '__main__':
    main()
