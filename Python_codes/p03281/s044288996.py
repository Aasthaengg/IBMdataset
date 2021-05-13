def main():
    n = int(input())

    ans = 0
    for num in range(1, n + 1, 2):
        cnt = 0
        for i in range(1, num + 1):
            if num % i == 0:
                cnt += 1
        if cnt == 8:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
