A, B, K = map(int, input().split())
a = []
b = []

for x in range(1, A + 1):
    if A % x == 0:
        a.append(x)

for y in range(1, B + 1):
    if B % y == 0 and y in a:
        b.append(y)

b = sorted(b,reverse = True)

print(b[K - 1])