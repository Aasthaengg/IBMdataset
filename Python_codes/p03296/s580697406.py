def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    cnt = 0

    for i in range(n - 1):
        if a_list[i] == a_list[i + 1]:
            a_list[i + 1] = -1
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
