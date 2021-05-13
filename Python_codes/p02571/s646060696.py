def solve(string):
    s, t = map(list, string.split())
    ans = len(t)
    for i in range(len(s)-len(t)+1):
        c = 0
        for j, _ in enumerate(t):
            c += 1 if s[i + j] != t[j] else 0
        ans = min(ans, c)
    return str(ans)

    pass


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
