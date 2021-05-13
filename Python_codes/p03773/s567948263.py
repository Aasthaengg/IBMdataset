i = [int(s) for s in input().split()]
A = (i[0] + i[1]) // 24
if A == 0:
    print(i[0] + i[1])
else:
    print((i[0] + i[1]) - 24)
