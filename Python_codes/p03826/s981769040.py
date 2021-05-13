i = [int(s) for s in input().split()]
a = i[0] * i[1]
at = i[2] * i[3]
if a < at:
    print(at)
else:
    print(a)
