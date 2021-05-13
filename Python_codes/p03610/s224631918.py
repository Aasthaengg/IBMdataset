s = input()

p = list(s)

even = []
odd = []

for i in range(len(p)):
    if (i + 1) % 2 == 1:
        odd.append(p[i])
    else:
        even.append(p[i])

for i in range(len(odd)):
    print(odd[i],end='')

print('')