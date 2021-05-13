def main():
    length = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count_operation = 0
    for i in range(length):
        if a[i] < b[i]:
            count_operation -= (b[i] - a[i]) // 2
        else:
            count_operation += a[i] - b[i]
    print("Yes" if count_operation <= 0 else "No")


if __name__ == '__main__':
    main()

