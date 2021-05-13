def main():
    n = int(input())
    a = [int(_) for _ in input().split()]

    order = [0 for i in range(n)]

    for i in range(n):
        order[a[i] - 1] = i + 1


#        order.append(a.index(i+1) + 1)

    print(*order)


if __name__ == '__main__':
    main()
