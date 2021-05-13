l = [2, 1]
for i in range(2, int(input()) + 1):
    l.append(l[len(l) - 1] + l[len(l) - 2])
print(l[len(l) - 1])