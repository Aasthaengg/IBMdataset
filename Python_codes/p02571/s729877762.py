def solve(string):
    s, t = map(list, string.split())
    ans = min(
        sum(1 if s[i + j] != t[j] else 0
            for j, _ in enumerate(t))
        for i in range(len(s) - len(t) + 1))
    return str(ans)

    pass


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
