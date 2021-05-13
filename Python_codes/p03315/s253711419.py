s = input()

num = 0
for c in s:
    if c == '+':
        num = num + 1
    else:
        num = num - 1
print(num)