def main():
    n, k = int(input()), int(input())
    x_list = list(map(int, input().split()))
    ans = 0

    for x in x_list:
        ans += 2 * min(x, k - x)

    print(ans)


if __name__ == "__main__":
    main()
