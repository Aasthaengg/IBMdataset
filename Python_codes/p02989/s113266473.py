def main():
    n = int(input())
    d_lst = list(map(int, input().split()))

    d_lst.sort()

    ans = d_lst[n // 2] - d_lst[n // 2 - 1]

    print(ans)


if __name__ == "__main__":
    main()
