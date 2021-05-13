a, b = [int(x) for x in input().split()]

cost = 0
if a >= 13:
    cost = b
elif a >= 6:
    cost = b / 2
else:
    cost = 0

print(int(cost))
