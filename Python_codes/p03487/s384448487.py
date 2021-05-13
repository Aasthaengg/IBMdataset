from collections import Counter


def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    counter = Counter(A)
    ans = 0
    for a, c in counter.items():
        if c < a:
            ans += c
        else:
            ans += c - a
    print(ans)


if __name__ == '__main__':
    main()
