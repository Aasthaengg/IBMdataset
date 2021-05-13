n = int(input())
a = 10 ** 9 + 7
b = 1

for i in range(1, n + 1):
    b *= i
    b %= a
print(b)