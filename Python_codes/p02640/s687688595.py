def main():
    x, y = map(int, input().split())

    for i in range(x + 1):
        total = i * 2 + (x - i) * 4
        if total == y:
            print("Yes")
            exit()
    else:
        print("No")


if __name__ == "__main__":
    main()
