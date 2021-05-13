ls = list(map(int, input().split()))
ls.sort()
if (ls[0] * ls[1] * ls[2]) % 2 == 0:
    print(0)
else:
    print(ls[0] * ls[1])
