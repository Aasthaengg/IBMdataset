def solve(n, s, t):
    if s == t:
        return n
    for common in range(n - 1, 0, -1):
        if s[-common:] == t[:common]:
            return 2 * n - common
    return 2 * n


n = int(input())
s = input()
t = input()
print(solve(n, s, t))
