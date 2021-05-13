#055_C
n, m = map(int, input().split())
m //= 2
if n > m:
    print(m)
else:
    print((n + m) // 2)