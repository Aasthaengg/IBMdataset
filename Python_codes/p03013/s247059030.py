def main():
    n, m = map(int, input().split())
    As = set([int(input()) for _ in range(m)])
    mod = 1000000007

    Steps = [0] * (n+1)
    Steps[0] = 1
    if 1 not in As:
        Steps[1] = 1

    for i in range(2, n+1):
        if i in As:
            continue
        Steps[i] = Steps[i-1] + Steps[i-2]
    ans = Steps[-1] % mod
    print(ans)


if __name__ == "__main__":
    main()
