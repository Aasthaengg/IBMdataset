arr = input().split(' ')
(a, b) = tuple((int(x) for x in arr))
area = a * b
circumference = (a + b) * 2
print(area, circumference)