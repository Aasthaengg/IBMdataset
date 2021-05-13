n = input()
a = input()
b = input()
c = input()
count = 0
for i in range(int(n)):
    d = set([a[i], b[i], c[i]])

    if len(d) == 3:
        count += 2
    elif len(d) == 2:
        count += 1
    else:
        pass

print(count)
