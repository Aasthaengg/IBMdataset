n, a, b = map(int, input().split())
ls = [int(input()) for _ in range(n)]


def check(k):
    return sum([(x - k * b + a - b - 1) // (a - b)
                for x in ls if x - k * b > 0]) <= k


m = max(ls)
lo = (m + a - 1) // a
hi = (m + b - 1) // b + 1
mi = (hi + lo) // 2
while hi > lo:
    mi = (hi + lo) // 2
    if check(mi):
        hi = mi
    else:
        lo = mi + 1
print(lo)