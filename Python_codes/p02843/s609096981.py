from itertools import product


def main():
    X = int(input())
    A, B, C, D, E= [(X // p) + 1 for p in range(100, 105)]

    P = product(range(A), range(B), range(C), range(D), range(E))
    flag = 0
    if X >= 100:
        for a, b, c, d, e in P:
            f = X - (a * 100 + b * 101 + c * 102 + d * 103 + e * 104)
            if f >= 0 and f % 105 == 0:
                flag = 1
                break

    print(flag)


if __name__ == '__main__':
    main()