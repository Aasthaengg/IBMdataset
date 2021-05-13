s = int(input())
a = [s]
while a[-1] not in a[:len(a)-2]:
    if a[-1] % 2 == 1:
        a.append(3 * a[-1] + 1)
    else:
        a.append(a[-1] // 2)
print(len(a))