x = [int(i) for i in input().split()]
x = sorted(x)
cost = 0
for i in range(1, 3):
    cost += abs(x[i] - x[i-1])
print(cost)