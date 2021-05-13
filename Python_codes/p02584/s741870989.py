# C - Walking Takahashi

x, k, d = map(int, input().split())

x = abs(x)

if x > d * k:
    print(x - d * k)
    exit()

k -= x // d
x %= d

print(x if k % 2 == 0 else d - x)
