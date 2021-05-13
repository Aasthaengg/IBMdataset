def main() -> None:
    N = int(input())
    B = [int(x) for x in input().split()]
    ans = B[0] + B[-1]
    for i in range(N - 2):
        ans += min(B[i], B[i+1])
    print(ans)


if __name__ == '__main__':
    main()
