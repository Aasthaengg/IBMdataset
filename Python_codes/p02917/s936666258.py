def main():
    n = int(input())
    b_list = list(map(int, input().split()))
    ans = b_list[0] + b_list[n - 2]

    for i in range(1, n - 1):
        ans += min(b_list[i - 1], b_list[i])

    print(ans)


if __name__ == "__main__":
    main()
