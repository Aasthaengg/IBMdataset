from collections import Counter


def main():
    n = int(input())
    As = list(int(input()) for _ in range(n))
    As_count = Counter(As)
    ans = 0
    for _, count in As_count.items():
        if (count % 2) == 0:
            continue
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
