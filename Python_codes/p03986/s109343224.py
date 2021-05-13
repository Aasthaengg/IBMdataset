x = list(map(str, input().rstrip()))

stock = 0
rest = 0
for i in x:
    if i == "S":
        stock += 1
    elif i == "T" and stock >= 1:
        stock -= 1
    else:
        rest += 1

print(stock + rest)