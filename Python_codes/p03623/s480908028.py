x, a, b = list(map(int, input().split()))
def MealDelivery(x, a, b):
    if abs(x -a) < abs(x -b):
        return 'A'
    elif abs(x -a) > abs(x -b):
        return 'B'
    else:
        return 'Even'
ans = MealDelivery(x, a, b)
print(ans)