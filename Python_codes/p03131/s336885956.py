k, a, b = map(int, input().split())
k += 1
if k <= a or a + 2 >= b:
    print(k)
    exit()
q = (k - a) // 2
r = (k - a) % 2
print(a + (b - a) * q + r)
