S = input()

t = 0
stock = 0
for c in S:
    if c == "S":
        stock += 1
    elif stock == 0:
        t += 1
    else:
        stock -= 1
print(t + stock)

