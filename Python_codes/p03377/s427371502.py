def main():
    a, b, x = map(int, input().split())
    if x < a:
        ans = "NO"
    else:
        if (x - a) > b:
            ans = "NO"
        else:
            ans = "YES"
    print(ans)


if __name__ == "__main__":
    main()
