a, b = map(str, input().split())

num1 = a * int(b)
num2 = b * int(a)
print(min(num1, num2))
