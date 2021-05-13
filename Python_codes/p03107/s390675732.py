from collections import Counter


def main():
    s = list(input())
    Count = Counter(s)
    if "0" not in s or "1" not in s:
        ans = 0
        print(ans)
        exit()
    min_key = min(Count, key=Count.get)
    ans = Count[min_key] * 2
    print(ans)


if __name__ == "__main__":
    main()
