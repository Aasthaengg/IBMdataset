def main():
    num = list(map(int, input().split()))
    num.sort()

    if sum(list(map(lambda x: x % 2, num))) == 3:
        print(num[0]*num[1])
    else:
        print(0)


if __name__ == "__main__":
    main()
