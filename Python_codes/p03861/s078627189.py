a, b, x = map(int, input().split())

count = 0
n = a % x
if (n == 0):
    c = a
else:
    c = a + (x - n)   # 最初の割れる数

if (c <= b):
    count += ((b - c) // x) + 1

print(count)