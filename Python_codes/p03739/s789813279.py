def main():
    n = int(input())
    A = list(map(int, input().split()))

    ans1 = 0
    total = 0
    is_plus = True
    for a in A:
        total += a

        if is_plus:
            if total <= 0:
                ans1 += -total + 1
                total = 1
        else:
            if total >= 0:
                ans1 += total + 1
                total = -1

        is_plus = not is_plus

    ans2 = 0
    total = 0
    is_plus = False
    for a in A:
        total += a

        if is_plus:
            if total <= 0:
                ans2 += -total + 1
                total = 1
        else:
            if total >= 0:
                ans2 += total + 1
                total = -1

        is_plus = not is_plus

    print(min(ans1, ans2))


if __name__ == "__main__":
    main()
