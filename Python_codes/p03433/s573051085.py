def main():
    n = int(input())
    a = int(input())

    mod = n % 500
    if mod <= a:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)


if __name__ == "__main__":
    main()
