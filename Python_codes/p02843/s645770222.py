def main():
    x = int(input())

    a_100 = x // 100
    b_100 = x % 100
    a_5 = b_100 // 5
    b_5 = b_100 % 5
    a_4 = b_5 // 4
    b_4 = b_5 % 4
    a_3 = b_4 // 3
    b_3 = b_4 % 3
    a_2 = b_3 // 2
    b_2 = b_3 % 2
    a_1 = b_2 // 1
    b_1 = b_2 % 1

    if a_5 + a_4 + a_3 + a_2 + a_1 > a_100:
        ans = 0
    else:
        ans = 1

    print(ans)


if __name__ == "__main__":
    main()
