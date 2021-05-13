from collections import Counter


def main():
    n = int(input())
    cnt = Counter()
    ans = 0
    for i in range(n):
        s = "".join(sorted(input()))
        if cnt[s] == 0:
            cnt[s] = 1
        else:
            ans += cnt[s]
            cnt[s] += 1
    print(ans)


if __name__ == "__main__":
    main()
