k = int(input())

lunlun = set([1,2,3,4,5,6,7,8,9])

for i in range(9):
    for x in list(lunlun):
        iti = int(str(x)[-1])
        l = x*10 + (iti-1)
        m = x*10 + (iti+0)
        n = x*10 + (iti+1)

        lunlun.add(m)
        if iti != 9:
            lunlun.add(n)
        if iti != 0:
            lunlun.add(l)

print(sorted(lunlun)[k-1])