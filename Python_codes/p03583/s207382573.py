import sys

input = sys.stdin.readline


def main():
    N = int(input())

    for h in range(1, 3501):
        for n in range(1, 3501):
            a = h * n * N
            b = 4 * h * n - (n + h) * N
            if b > 0 and a % b == 0:
                w = a // b
                print(h, n, w)
                exit()


if __name__ == "__main__":
    main()
