A, B, C = map(int,open(0).read().split())
if (A * B * C) % 2 == 0:
    print("0")
else:
    ABClist = [A, B, C]
    newlist = sorted(ABClist)
    print(newlist[0] * newlist[1])