from collections import Counter


def main():
    n, k = map(int, input().split())
    As = map(int, input().split())
    ans = 0
    for num, count in Counter(As).most_common()[::-1][:-k]:
        ans += count
    print(ans)


if __name__ == "__main__":
    main()
