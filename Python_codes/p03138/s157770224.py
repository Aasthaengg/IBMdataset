n, k = map(int, input().split())
a = list(map(int, input().split()))
memo = {}

def doit(k):
    if not k in memo:
        if k == 0:
            memo[k] = sum(a)
        else:
            b = 1
            while k >= b:
                b *= 2
            b = b // 2
            d = 0
            for ai in a:
                d += b if ai & b == 0 else -b
            memo[k] = max(d + doit(k - b), doit(b - 1))
    return memo[k]

print(doit(k))
