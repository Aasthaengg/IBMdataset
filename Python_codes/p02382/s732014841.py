input()
x = list(map(int, input().split()))
y = list(map(int, input().split()))
l = []
for a, b in zip(x, y):
  l += [abs(a - b)]
print("{0:.6f}".format(sum(l)))
print("{0:.6f}".format(sum([e ** 2 for e in l]) ** 0.5))
print("{0:.6f}".format(sum([e ** 3 for e in l]) ** (1/3)))
print("{0:.6f}".format(max(l)))
