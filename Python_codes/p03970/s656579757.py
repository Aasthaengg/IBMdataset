s = input()
c = 0
for i, j in zip('CODEFESTIVAL2016', s):
    if i != j:
        c += 1
print(c)
