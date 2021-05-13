s = input()
l = []
b = 0

for i in s:
    if b == 1:
        l.append(i)
    if i == 'A' and b == 0:
        l.append(i)
        b = 1

z = [i for i, x in enumerate(l, 1) if x == 'Z']
print(max(z))
