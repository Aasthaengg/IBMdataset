from collections import Counter


def main():
    abc = list(map(int, input().split()))
    ans = Counter(abc).most_common()[-1][0]
    print(ans)


if __name__ == "__main__":
    main()
