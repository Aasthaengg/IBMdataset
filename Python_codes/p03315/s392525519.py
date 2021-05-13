S = str(input())

num = 0

for i in S:
    if i == "+":
        num += 1
    elif i == "-":
        num -= 1
print(num)