from collections import defaultdict


def main():
    a = input()
    cnt = defaultdict(lambda: 0)
    for aa in a:
        cnt[aa] += 1
    ans = len(a) * (len(a) - 1) // 2 + 1
    for c, n in cnt.items():
        ans -= n * (n - 1) // 2
    print(ans)


if __name__ == '__main__':
    main()

