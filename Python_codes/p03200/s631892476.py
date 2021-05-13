mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    S = input().rstrip('\n')
    ans = 0
    cnt = 0
    for s in S:
        if s == "B":
            cnt += 1
        else:
            ans += cnt
    print(ans)


if __name__ == '__main__':
    main()
