s = input()
c1 = 0
c0 = 0
for i in s:
    if i == '0':
        c0 += 1
    else:
        c1 += 1
print(2*min(c0, c1))