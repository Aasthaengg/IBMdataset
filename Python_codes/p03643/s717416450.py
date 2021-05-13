def main():
    N = input()
    ans = "000"

    if len(N) == 1:
        ans = "ABC00" + N
    elif len(N) == 2:
        ans = "ABC0" + N
    else:
        ans = "ABC" + N

    print(ans)


if __name__ == "__main__":
    main()
