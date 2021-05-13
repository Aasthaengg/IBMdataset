def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    is_ok = True

    for a in a_lst:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                is_ok = False

    if is_ok:
        ans = "APPROVED"
    else:
        ans = "DENIED"

    print(ans)


if __name__ == "__main__":
    main()
