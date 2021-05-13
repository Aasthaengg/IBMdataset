def main():
    N = int(input())
    power = 1
    for i in range(1, N + 1):
        power *= i
        power %= 10 ** 9 + 7
    print(power)


if __name__ == "__main__":
    main()
