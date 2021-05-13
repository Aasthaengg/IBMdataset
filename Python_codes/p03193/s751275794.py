nhw = input().split()
n = int(nhw[0])
h = int(nhw[1])
w = int(nhw[2])

ablist = []
for i in range(n):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    ablist.append((a, b))


count = 0
for a, b in ablist:
    if a >= h and b >= w:
        count += 1

print(count)
