def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    ans = 1

    if 0 in set(a_lst):
        ans = 0
    else:
        for a in a_lst:
            ans *= a
            if ans > 10 ** 18:
                ans = -1
                break

    print(ans)


if __name__ == "__main__":
    main()
