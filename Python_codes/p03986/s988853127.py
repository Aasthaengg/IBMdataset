x = input()
num = [0]
for i in x:
    if i == "S":
        num.append(num[-1] - 1)
    else:
        num.append(num[-1] + 1)
print(max(max(num), 0) * 2)