values = []
while True:
    value = input().split()
    if int(value[0]) == 0 and int(value[1]) == 0:
        break
    else:
        values.append(value)

for value in values:
    m = int(value[0])
    n = int(value[1])
    for i in range(m):
        row_output = ""
        for j in range(n):
            row_output += "#" if (i + j) % 2 == 0 else "."
        print(row_output)
    print()

