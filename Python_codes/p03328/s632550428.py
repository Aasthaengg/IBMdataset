a, b = map(int, input().split())

diff = b - a
alen = ((diff-1) * diff) // 2
print(alen - a)
