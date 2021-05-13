from math import sqrt

a, b, c = map(int, input().split())

left = 4 * a * b

r = c - (a + b)
right = r * r

if r < 0 and sqrt(left) < abs(r):
    left = -left
    right = -right

if left < right:
    print("Yes")
else:
    print("No")
