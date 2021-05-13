def main():
    n = int(input())

    for x in range(n, 1000):
        if str(x)[0] == str(x)[1] == str(x)[2]:
            print(x)
            break


if __name__ == "__main__":
    main()
