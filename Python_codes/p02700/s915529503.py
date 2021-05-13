a, b, c, d = map(int, input().split())
while a > 0 and c > 0:
    c -= b
    a -= d
print('Yes') if a > 0 or (a <= 0 and c <= 0) else (print('No'))
