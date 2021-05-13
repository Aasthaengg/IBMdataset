n = input()
xs = map(float, input().split())
ys = map(float, input().split())
abs_d = [abs(x - y) for (x, y) in zip(xs, ys)]
d = [sum([i ** p for i in abs_d]) ** (1 / p) for p in range(1, 4)]
d.append(max(abs_d))

print(*d, sep='\n')
