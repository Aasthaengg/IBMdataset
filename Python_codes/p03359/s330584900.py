a, b = map(int, input().split())

num = 0
for i in range(12):
    if i < a:
        num += 1
if a > b:
    num -= 1

print(num)