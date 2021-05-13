x = int(input())
n = x // 11
x %= 11
if x == 0:
    print(2 * n)
else:
    print(2 * n + (x - 1) // 6 + 1)