a = input()

s = 0
for x in a:
    if x == "+":
        s += 1
    else:
        s -= 1

print(s)