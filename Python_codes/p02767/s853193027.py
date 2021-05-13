n, *x = map(int, open(0).read().split())
print(min([sum([(a - i) ** 2 for a in x]) for i in range(1, 101)]))