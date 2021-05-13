def main():
    while True:
        num = input()

        if num == "0":
            break

        print(sum([int(x) for x in num]))

if __name__ == '__main__':
    main()
