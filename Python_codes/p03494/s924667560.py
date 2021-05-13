def main():
    n = int(input())
    a = list(map(int, input().split()))

    min_two_count = 2 ** 30

    for i in range(len(a)):
        temp_two_count = 0
        while a[i] % 2 == 0:
            temp_two_count += 1
            a[i] = a[i] // 2

        if min_two_count > temp_two_count:
            min_two_count = temp_two_count

    print(min_two_count)


if __name__ == "__main__":
    main()
