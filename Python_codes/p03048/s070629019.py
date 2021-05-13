def main():
    R, G, B, N = map(int, input().split())

    ans = 0
    for i in range(N+1):
        for j in range(N+1):
            tmp = N - i * R - j * G
            if tmp % B == 0 and tmp >= 0:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
