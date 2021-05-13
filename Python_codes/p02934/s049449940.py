n = int(input())
a = tuple(map(int, input().split()))
x = 1
for i in a:
    x *= i
y = 0
for i in a:
    y += x // i
print(x / y)