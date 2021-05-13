def main():
    S = input()
    T = input()

    if S == T[0:-1]:
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
