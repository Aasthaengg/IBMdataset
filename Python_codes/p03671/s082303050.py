a, b, c = map(int, input().split())
cost1 = a + b
cost2 = a + c
cost3 = b + c
print(min(cost1, cost2, cost3))