a, b = map(float, input().split())

a = round(a)
b = round(b*100)

print(a * b // 100)