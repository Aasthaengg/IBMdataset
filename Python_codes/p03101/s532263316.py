h, w = map(int, input().split())
a, b = map(int, input().split())
lm = h * w
sm = (a * w + h * b) - a * b
print(int(lm - sm))
