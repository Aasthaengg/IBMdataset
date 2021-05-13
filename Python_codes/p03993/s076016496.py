def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    cnt = 0

    for i in range(n):
        if a_list[a_list[i] - 1] - 1 == i:
            cnt += 1

    print(cnt // 2)


if __name__ == "__main__":
    main()
