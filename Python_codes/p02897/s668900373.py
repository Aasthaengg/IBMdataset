
def main():
    n = int(input())
    if n % 2 == 1:
        print(float(((n // 2) + 1) / n))
    else:
        print(float((n / 2) / n))


if __name__ == "__main__":
    main()
