import math


def f2(n):
    d = 0
    c = 0
    for i in range(1, n):
        e = 0
        if i * i == n:
            e -= 1
        elif n % i == 0:
            e -= 1
        e += n // i
        d += e

    return d

def main():
    print(f2(int(input())))


if __name__ == '__main__':
    main()
