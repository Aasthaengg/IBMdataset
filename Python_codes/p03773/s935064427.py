def main():
    a, b = map(int, input().split())
    if a+b <= 23:
        ans = a+b
    else:
        ans = (a+b)-24
    print(ans)


if __name__ == "__main__":
    main()
