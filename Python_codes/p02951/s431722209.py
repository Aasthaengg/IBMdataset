a, b, c = map(int, input().split())

while b < a:
    c -= 1
    b += 1
    if c == 0:
        break

print(c)
