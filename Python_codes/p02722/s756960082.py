import math


def list_divisor(n):
    divisor1 = {1}
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor1.add(i)

    divisor2 = {n}
    for i in divisor1:
        divisor2.add(n // i)

    return divisor1 | divisor2


def main():
    n = int(input().rstrip())

    sub_only = len(list_divisor(n - 1)) - 1

    div_included = 0
    for d in (list_divisor(n) - {1}):
        n1 = n // d
        while n1 % d == 0:
            n1 = n1 // d

        if n1 == 1:
            div_included += 1
            continue

        if d in list_divisor(n1 - 1):
            div_included += 1

    print(sub_only + div_included)


if __name__ == '__main__':
    main()
