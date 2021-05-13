def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    x = N - K + 1
    ans = [x]
    for i in range(2, K + 1):
        x = ((x * (N - K + 2 - i) * (K - i + 1) // (i * (i - 1))))
        ans.append(x % MOD)
    print ('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()
