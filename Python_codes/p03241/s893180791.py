n, m = map(int, input().split())
a, r = divmod(m, n)
while True:
    r = m%a
    if r == 0:
        break
    a -= 1
print(a)
