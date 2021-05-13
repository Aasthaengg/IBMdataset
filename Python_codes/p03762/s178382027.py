def wa(ka, li):
    t = 0
    i = 0
    while ka > 0:
        t = (t + (li[-(i + 1)] - li[i]) * (ka - 1)) % (10 ** 9 + 7)
        ka -= 2
        i += 1
    return t


n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
print(wa(n, x)*wa(m, y) % (10**9+7))