def main():
    h = int(input())
    num = 1
    ans = 1

    while True:  # h以上で最小の2の累乗を探す
        num *= 2
        if h < num:
            break
        elif h == num:
            ans = 2 * ans + 1
            break
        ans = 2 * ans + 1

    print(ans)


if __name__ == "__main__":
    main()
