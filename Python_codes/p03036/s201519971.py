factor, sub, year = map(int, input().split())
weight = 0

for x in range(1, 11):
    if x == 1:
        weight = factor * year * x - sub
    else:
        weight = factor * weight - sub
    print(weight)
