def main():
    n = int(input())
    l_list = list(map(int, input().split()))

    sum_l = sum(l_list)
    max_l = max(l_list)

    if max_l < sum_l - max_l:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
