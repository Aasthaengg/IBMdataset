n = int(input())

l = list()
l.append(2)
l.append(1)

for a in range(1, n):
    l.append(l[a] + l[a-1])

print(l[-1])
