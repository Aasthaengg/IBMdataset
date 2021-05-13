s = input()
l = len(s)
X, Y = (int(x) for x in input().split())
F = s.split("T")
x_move = [f.count("F") for f in F[2::2]]
y_move = [f.count("F") for f in F[1::2]]
x_set = set()
x_set.add(F[0].count("F"))
y_set = set()
y_set.add(0)
for move in x_move:
    x_set = set(x + move for x in x_set) | set(x - move for x in x_set)
for move in y_move:
    y_set = set(y + move for y in y_set) | set(y - move for y in y_set)

if X in x_set and Y in y_set:
    print("Yes")
else:
    print("No")
