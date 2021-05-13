A, B = map(int, input().split())
if A <= 5:
    cost = 0
elif A <= 12:
    cost = B / 2
else:
    cost = B
print(int(cost))