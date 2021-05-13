def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))

    a_sort = sorted(a)
    a_max = a_sort[-1]
    a_second = a_sort[-2]

    for i in range(n):
        if a[i] == a_max:
            print(a_second)
        else:
            print(a_max)


if __name__ == '__main__':
    main()
