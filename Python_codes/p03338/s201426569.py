from string import ascii_lowercase


def cut_and_count(s, n, i):
    x = set(s[:i])
    y = set(s[i:])
    cnt = 0

    for ch in ascii_lowercase:
        if ch in x and ch in y:
            cnt += 1
    return cnt


def main():
    n = int(input())
    s = list(input())
    ans = 0

    for i in range(1, n):
        res = cut_and_count(s, n, i)
        ans = max(ans, res)

    print(ans)


if __name__ == "__main__":
    main()
