x = input()

stock = 0
rest = len(x)

for a in x:
    if a == "S":
        stock += 1
    else:
        if stock > 0:
            stock -= 1
            rest -= 2
        else:
            stock = 0

print(rest)