def main():
    a, b = input().split()

    if int(int(a + b) ** 0.5) ** 2 == int(a + b):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
