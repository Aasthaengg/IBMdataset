def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    ans = 0
    cnt = 0

    for i in range(n - 1):
        if h_list[i] >= h_list[i + 1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0

    print(max(ans, cnt))


if __name__ == "__main__":
    main()
