a = input()
b = input()

c = 0
for i, j in zip(a, b):
    if i != j:
        c += 1
print(c)