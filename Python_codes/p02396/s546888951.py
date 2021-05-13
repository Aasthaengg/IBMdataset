b = []
i = 1
while 1:
    x = int(input())
    b.append(x)
    if x == 0:
        break

for x in b:
    if x == 0:
        break
    print("Case ", (i), ': ', (x), sep='')
    i += 1