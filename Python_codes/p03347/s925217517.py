def solve(n, aaa):
    if aaa[0] > 0:
        return -1
    if any(a1 - a0 > 1 for a0, a1 in zip(aaa, aaa[1:])):
        return -1
    ans = 0
    a0 = 0

    for a1 in aaa[1:]:
        if a1 - a0 != 1:
            ans += a0
        a0 = a1

    return ans + a0


n = int(input())
aaa = list(map(int, (input() for _ in range(n))))
print(solve(n, aaa))
