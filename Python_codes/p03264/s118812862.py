k = int(input())

od = []
ev = []

for i in range(1,k+1):
    if i % 2 == 0:
        ev.append(i)
    else:
        od.append(i)

print(len(od)*len(ev))