def main():
    h, n = map(int, input().split())
    a_lst = list(map(int, input().split()))

    if sum(a_lst) >= h:
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
