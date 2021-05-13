def solve(n, a):
    if a[0] != 0:
        return -1

    if any(x > 1 for x in (t - s for s, t in zip(a, a[1:]))):
        return -1

    p = None
    ans = 0
    for c in reversed(a):
        if p is None or c != (p - 1):
            ans += c
        p = c
    return ans


if __name__ == '__main__':
    n = int(input())
    a = [int(input()) for _ in range(n)]
    print(solve(n, a))

# 単調非減少
# 差分は0/1
