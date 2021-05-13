x = int(input())
a = int(input())
b = int(input())
left = 0
left = x - a
left -= b * int(left / b)
print(left)