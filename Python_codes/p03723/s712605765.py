def main2():
    A, B, C = map(int, input().split())

    ans = 0
    if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
        print(ans)
        exit()

    elif (2 * A - B - C) == 0 and (2 * B - A - C) == 0 and (2 * C - A - B) == 0:
        print(-1)
        exit()

    else:
        while True:
            if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
                print(ans)
                exit()

            A, B, C = (B + C)//2, (A + C)//2, (A + B)//2
            ans += 1


if __name__ == "__main__":
    main2()