A, B = [int(s) for s in input().split()]
if (A - B) % 2 == 0:
    print((A+B)//2)
else:
    print("IMPOSSIBLE")
