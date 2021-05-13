n, a, b = [int(item) for item in input().split()]
x = [int(item) for item in input().split()]

cost = 0
for i in range(1, n):
    walk = (x[i] - x[i-1]) * a 
    if walk > b:
        cost += b
    else:
        cost += walk
print(cost)