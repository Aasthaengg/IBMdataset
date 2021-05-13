n, x, t = map(int, input().split())

r = n//x
if n % x != 0:
    r += 1

print(r*t)
