k = int(input())
n = 50
a = k // n
b = k % n
print(n)
for i in range(b):
    print(n - 1 + a + 50 - (b - 1), end = " ")
for i in range(n - b):
    print(n - 1 + a - b, end = " ")