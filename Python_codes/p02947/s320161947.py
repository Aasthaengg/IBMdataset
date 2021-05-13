from collections import defaultdict

def main():
    N = int(input())
    strs = defaultdict(int)
    for _ in range(N):
        str = list(input().rstrip())
        strs[''.join(sorted(str))] += 1

    ans = 0
    for freq in strs.values():
        if freq > 1:
            ans += (freq * (freq - 1)) // 2
    print(ans)


if __name__ == '__main__':
    main()
