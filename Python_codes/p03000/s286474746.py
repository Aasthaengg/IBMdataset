def main():
    n, x = map(int, input().split())
    l_lst = list(map(int, input().split()))
    count = 0
    coordinate_lst = [0]

    for i in range(n):
        coordinate_lst.append(coordinate_lst[i] + l_lst[i])

    for i in range(n+1):
        if coordinate_lst[i] <= x:
            count += 1

    print(count)


if __name__ == '__main__':
    main()