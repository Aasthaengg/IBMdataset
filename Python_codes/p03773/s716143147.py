a, b = list(map(int, input().split()))
h = a + b
if h >= 24:
    h = h - 24
print(h)