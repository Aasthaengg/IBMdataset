x = int(input())
l = [i**5 for i in range(10000)]
for idx, a in enumerate(l):
    b = a - x
    if b in l:
        print(idx, l.index(b))
        exit()
    elif -b in l:
        print(idx, -l.index(abs(b)))
        exit()