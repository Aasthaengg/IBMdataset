x = int(input())
si = 0
i = 1
while True:
    nsi = si + i
    if si < x <= nsi:
        break
    si = nsi
    i += 1

print(i)
