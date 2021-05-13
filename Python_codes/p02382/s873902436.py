n = int(input())
x = map(int, input().split())
y = map(int, input().split())

n_vec = zip(x, y)

xy_diff = [abs(xi - yi) for xi, yi in n_vec]

Ma_d = sum(xy_diff)
Eu_d = sum([i ** 2 for i in xy_diff]) ** 0.5
Mi3_d = sum([i ** 3 for i in xy_diff]) ** (1 / 3)
Ch_d = max(xy_diff)

print("{0}\n{1}\n{2}\n{3}".format(Ma_d, Eu_d, Mi3_d, Ch_d))