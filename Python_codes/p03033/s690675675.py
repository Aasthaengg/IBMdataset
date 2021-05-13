from bisect import bisect_left

def solve(n, q, s, t, x, d):
    v = sorted(list(zip(s, t, x)), key=lambda _:_[2])
    res = [-1] * q
    jump = [-1] * q
    for s, t, x in v:
        l = bisect_left(d, s - x)
        r = bisect_left(d, t - x)
        while l < r:
            s = jump[l]
            if s == -1:
                res[l] = x
                jump[l] = r
                l += 1
            else:
                l = s
    return res

n, q = map(int, input().split())
s = [-1] * n
t = [-1] * n
x = [-1] * n
for i in range(n):
    s[i], t[i], x[i] = map(int, input().split())
d = [int(input()) for i in range(q)]

print(*solve(n, q, s, t, x , d), sep="\n")