n = int(input())
s = input()
cost = 0
bc = 0
for it in s:
    if it =="#":
        bc += 1
    else:
        if bc > 0:
            cost += 1
            bc -= 1
print(cost)
