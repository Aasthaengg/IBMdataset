def solve(s, t):
    n = len(s)
    m = len(t)
    if n < m:
        return 'UNRESTORABLE'
    for i in range(n-m+1)[::-1]:
        if all([s[i+j] == '?' or s[i+j] == t[j] for j in range(m)]):
            return s[:i].replace('?', 'a') + t + s[i+m:].replace('?', 'a')
    return 'UNRESTORABLE'


def main():
    s = input()
    t = input()
    print(solve(s, t))


if __name__ == "__main__":
    main()
