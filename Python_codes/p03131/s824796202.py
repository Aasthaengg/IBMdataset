k, a, b = map(int, input().split())

if k <= a - 1 or a + 1 >= b:
    print(k + 1)
    exit()
k -= a - 1

print(a + k // 2 * (b - a) + k % 2)
