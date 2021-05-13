def main():
    L, R = map(int, input().split())
    R = min(R, L + 4038)
    ans = 2018

    for i in range(L, R + 1):
        for j in range(i + 1, R + 1):
            ans = min(ans, (i*j) % 2019)

    print(ans)

if __name__ == "__main__":
    main()