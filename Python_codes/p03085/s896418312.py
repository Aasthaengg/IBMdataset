b = input()
x = ['A', 'C', 'T', 'G']

for i in range(4):
    if b == x[i]:
        print(x[(i + 2) % 4])
        break
