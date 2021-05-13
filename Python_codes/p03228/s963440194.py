def main():
    a, b, k = [int(abk) for abk in input().split(" ")]

    for i in range(k):

        if i % 2 == 0:

            if a % 2 == 1:
                a = present_for_b = (a - 1) / 2

            else:
                a = present_for_b = a / 2

            b = b + present_for_b

        else:

            if b % 2 == 1:
                b = present_for_a = (b - 1) / 2

            else:
                b = present_for_a = b / 2

            a = a + present_for_a

    print("{a} {b}".format(a=str(int(a)), b=str(int(b))))


if __name__ == "__main__":
    main()
