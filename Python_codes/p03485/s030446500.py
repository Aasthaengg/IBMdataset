a, b = map(int, input().split())
if (a % 2 != 0) or (b % 2 != 0):
    a += 1
print(int((a + b) / 2))