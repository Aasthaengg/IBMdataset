def calc_num_digits(x):
    num_digits = 0
    while True:
        if x // 10 == 0:
            num_digits += 1
            break
        x //= 10
        num_digits += 1
    return num_digits


def main():
    n = int(input())
    ans = 0

    for i in range(1, n + 1):
        num_digits = calc_num_digits(i)
        if num_digits % 2 == 1:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
