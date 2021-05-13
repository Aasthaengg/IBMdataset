from collections import Counter


def main():
    n = int(input())
    As = list(map(int, input().split()))
    ans = 0
    for num, count in Counter(As).items():
        if count >= num:
            ans += (count - num)
        else:
            ans += count
    print(ans)


if __name__ == "__main__":
    main()
