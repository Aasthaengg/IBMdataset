#!python3

# input
N = int(input())

MOD = 10 ** 9 + 7


def main():
    x = 1
    for i in range(1, N + 1):
        x = x * i % MOD
    print(x)


if __name__ == "__main__":
    main()
