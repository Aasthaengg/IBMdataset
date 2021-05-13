def main():
    lst = list(map(int, input().split()))
    lst.sort()

    for l in lst:
        if l % 2 == 0:
            print(0)
            exit()
    print(lst[0] * lst[1])


if __name__ == "__main__":
    main()
