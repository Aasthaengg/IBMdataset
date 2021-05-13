values = list(map(int, input().split(' ')))

m = max(values)
values.remove(m)

print(10 * m + sum(values))
