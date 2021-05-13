def main():
    apples = int(input())
    count = 0
    for _ in range(apples):
        if int(input()) % 2 == 0:
            count += 1
    print("first" if count != apples else "second")


if __name__ == '__main__':
    main()

