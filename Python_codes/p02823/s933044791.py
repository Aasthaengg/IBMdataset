n, a, b = map(int, input().split())
a = min(a, b)
b = max(a, b)

ret = 0
if (b - a) & 1:
    if n - a < b - 1:
        ret = n - b + 1
        a += ret
        b = n
    else:
        ret = a
        a = 1
        b -= ret
print(ret + (b - a) // 2)
