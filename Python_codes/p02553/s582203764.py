a, b, c, d = list(map(int, input().split(' ')))
mul = [a*c, a*d, b*c, b*d]
print(max(mul))