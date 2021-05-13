n, k, *xx = map(int, open(0).read().split())

print(2 * sum(min(abs(x), abs(k-x)) for x in xx))