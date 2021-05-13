import sys

input = sys.stdin.readline


def main():
    r, D, x_2000 = map(int, input().split())

    x_prev = x_2000
    for i in range(10):
        x = r * x_prev - D
        print(x)
        x_prev = x


if __name__ == "__main__":
    main()
