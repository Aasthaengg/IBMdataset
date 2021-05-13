n = int(input())
xs = [int(x) for x in input().split()]

ys = map(lambda x: 1. / x, xs)
print(1. / sum(list(ys)))