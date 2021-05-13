n, d = map(int, input().split())
a = 0
b = 0
while a < n:
    a = d*2 + 1 + a
    b = b + 1
print(b)