N = int(input())

amount = 0

for i in range(1, N + 1):
    if (i % 15 == 0) or (i % 3 == 0) or (i % 5 == 0):
        pass
    else:
        amount = amount + i

print(amount)
