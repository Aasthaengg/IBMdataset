a, b = map(int, input().split())

if a > b:
    c = a
    a -= 1
else:
    c = b
    b -= 1

print(c+max(a, b))