def main():
    n = input()
    if n == "1":
        print("Hello World")
    else:
        print(sum([int(input()) for _ in range(2)]))


if __name__ == '__main__':
    main()

