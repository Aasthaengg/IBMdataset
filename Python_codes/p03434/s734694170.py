N = int(input(""))
a = input("").split(" ")
a = [int(aa) for aa in a]
ap = 0
bp = 0
temp = 0
for c in range(len(a)):
    if c % 2 == 0:
        temp = a.pop(a.index(max(a)))
        ap += temp
    else:
        temp = a.pop(a.index(max(a)))
        bp += temp
print(str(abs(ap-bp)))