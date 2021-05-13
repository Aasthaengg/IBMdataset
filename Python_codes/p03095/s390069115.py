def main():
    N = int(input())
    S = input()
    MOD = 10**9 + 7
    from collections import Counter
    c = Counter(S)
    ans = 1
    for v in c.values():
        ans *= (v+1)
        ans %= MOD
    print(ans-1)


if __name__ == '__main__':
    main()
