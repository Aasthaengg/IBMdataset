a, b, c, d = map(int, input().split())

square1 = a * b
square2 = c * d

ans = 0
if square1 < square2:
    ans = square2
else:
    ans = square1

print(ans)