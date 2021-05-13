from collections import Counter


def main():
    n, m = map(int, input().split())
    a = Counter(list(map(int, input().split())))
    cards = []
    for i, v in a.items():
        cards.append([i, v])
    for _ in range(m):
        cards.append(list(map(int, input().split()))[::-1])
    cards.sort(key=lambda x: x[0], reverse=True)
    ans = 0
    for i, v in cards:
        ans += i * min(v, n)
        n -= min(v, n)
    print(ans)


if __name__ == '__main__':
    main()

