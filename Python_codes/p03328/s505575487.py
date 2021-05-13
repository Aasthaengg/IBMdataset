a, b = map(int, input().split())
x = b - a
tmp = 0
for i in range(1, x):
    tmp += i
print(tmp - a)