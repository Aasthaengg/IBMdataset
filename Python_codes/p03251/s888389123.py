n, m, x, y = [int(i) for i in input().split()]
x_list = [int(i) for i in input().split()] + [x]
y_list = [int(i) for i in input().split()] + [y]
print("No War" if max(x_list) < min(y_list) else "War")