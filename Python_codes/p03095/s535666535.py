from collections import Counter


def main():
    MOD = 10**9 + 7
    N = int(input())
    counter = Counter(input())
    ans = 1
    for c in counter.values():
        ans *= c + 1
        ans %= MOD
    print(ans - 1)


if __name__ == '__main__':
    main()