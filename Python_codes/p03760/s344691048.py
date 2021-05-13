O = list(input())
E = list(input())

for i in range(len(E)):
    O.insert(2 * i + 1, E[i])

print("".join(O))