c = []
for i in range(3):
    c.append(input())

for i in range(3):
    for j in range(3):
        if i == j:
            print(c[i][j],end="")
print()
