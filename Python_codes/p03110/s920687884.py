def main():
    n = int(input())
    gift = 0

    for _ in range(n):
        x, u = input().split()
        if u == "JPY":
            gift += int(x)
        else:
            gift += float(x) * 380000

    print(gift)


if __name__ == "__main__":
    main()
