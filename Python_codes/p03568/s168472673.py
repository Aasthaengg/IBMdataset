def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    even_count = 0

    for a in a_list:
        if a % 2 == 0:
            even_count += 1

    print(3 ** n - 2 ** even_count)


if __name__ == "__main__":
    main()
