def main():
    N, T = map(int, input().split())
    t = list(map(int, input().split()))

    ans = 0
    for i in range(1, N):
        if t[i]-t[i-1] >= T:
            ans += T
        else:
            ans += (t[i]-t[i-1])
    ans += T

    print(ans)


if __name__ == "__main__":
    main()
