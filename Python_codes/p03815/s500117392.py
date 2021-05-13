x = int(input())
c = 2 * (x // 11)
if x % 11 == 0:
    pass
elif x - 11 * (x // 11) > 6:
    c += 2
else:
    c += 1
print(c)
