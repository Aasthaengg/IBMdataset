def main():
    month, day = map(int, input().split(" "))
    if month > day:
        month -= 1
    print(month)


if __name__ == '__main__':
    main()