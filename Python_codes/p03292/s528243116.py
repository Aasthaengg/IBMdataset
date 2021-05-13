a = sorted(list(map(int,input().split())))

cost_a = a[1] - a[0]
cost_b = a[2] - a[1]
print(cost_a + cost_b)