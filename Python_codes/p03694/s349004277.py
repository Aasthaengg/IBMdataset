def main():
    n = int(input())
    As = list(map(int, input().split()))
    As = sorted(As)

    ans = 0
    for i in range(n-1):
        ans += As[i+1] - As[i]

    print(ans)


if __name__ == "__main__":
    main()
