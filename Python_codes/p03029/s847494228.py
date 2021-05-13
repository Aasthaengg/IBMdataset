x = [int(i) for i in input().split()]

if x[0] < 1 and x[1] < 2:
    print(0)
else:
    print(((x[0] * 3) + x[1]) // 2)