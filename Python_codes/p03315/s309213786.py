s = input()
num = 0
for eat in s:
    if eat == '+':
        num += 1
    else:
        num -= 1
print(num)
