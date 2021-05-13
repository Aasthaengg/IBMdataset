def main():
    n = int(input())
    As = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        temp = As[i]
        if temp % 2 == 0:
            cnt = 0
            while temp % 2 == 0:
                cnt += 1
                temp //= 2
            ans += cnt

    print(ans)


if __name__ == "__main__":
    main()
