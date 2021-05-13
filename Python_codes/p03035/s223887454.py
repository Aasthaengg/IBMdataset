inp = input().split()

age = int(inp[0])
cost = int(inp[1])

if age >= 13: print(cost)
elif age >= 6: print(int(cost/2))
else: print(0)
