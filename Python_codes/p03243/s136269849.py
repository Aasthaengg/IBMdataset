def main():
    n = int(input())

    for i in range(1, 10):
        if n <= i * 111:
            print(i * 111)
            break


if __name__ == "__main__":
    main()
