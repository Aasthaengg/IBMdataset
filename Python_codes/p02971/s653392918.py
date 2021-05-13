def main():
    n = int(input())
    a_lst = [int(input()) for _ in range(n)]

    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]

    biggest = 0
    for i in range(n):
        if biggest < a_lst[i]:
            biggest = a_lst[i]
        left[i] = biggest

    biggest = 0
    for i in range(n - 1, -1, -1):
        if biggest < a_lst[i]:
            biggest = a_lst[i]
        right[i] = biggest

    print(right[1])
    for i in range(1, n - 1):
        print(max(left[i - 1], right[i + 1]))
    print(left[-2])


if __name__ == "__main__":
    main()
