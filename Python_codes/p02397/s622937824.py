matrix = []
while True:
    values = input()
    i_list = [int(x) for x in values.split()]
    if 2 == i_list.count(0):
        break
    matrix.append(i_list)

for i in matrix:
    a, b = sorted(i)
    print(a, b)