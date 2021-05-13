x = [input() for i in range(2)]
count = 0
for i in range(3):
    if x[0][i] == x[1][i]:
        count += 1
print(count)
