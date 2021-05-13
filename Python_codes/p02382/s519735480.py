from functools import reduce

n = input()
xs = map(float, input().split())
ys = map(float, input().split())

d = list(map(lambda x, y: abs(x - y), xs, ys))
ds = [sum([i ** p for i in d]) ** (1 / p) for p in range(1, 4)]
ds.append(max(d))

print(reduce(lambda h, t: h + '\n' + t, [str(e) for e in ds]))