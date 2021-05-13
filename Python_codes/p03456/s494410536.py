a, b = map(int, input().split())

ab = None
for i in range(1, 4):
    if b == b%(10**i):
        ab = a*(10**i) + b
        break

for i in range(1, 1000):
    if i**2 == ab:
        print('Yes')
        exit()

print('No')
