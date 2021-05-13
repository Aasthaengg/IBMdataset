# D - FT Robot

s = input()
x, y = map(int, input().split())

f = [len(x) for x in s.split("T")]
x -= f[0]
fx = f[2::2]
fy = f[1::2]

x_possible_set = set([0])
for dx in fx:
    x_possible_set = set([xi + dx for xi in x_possible_set] + [xi - dx for xi in x_possible_set])

y_possible_set = set([0])
for dy in fy:
    y_possible_set = set([yi + dy for yi in y_possible_set] + [yi - dy for yi in y_possible_set])

print("Yes" if x in x_possible_set and y in y_possible_set else "No")