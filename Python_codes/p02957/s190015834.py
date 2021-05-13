A, B = [int(i) for i in input().split()]
if (A + B) / 2 == (A + B) // 2:
    print((A + B) // 2)
else:
    print("IMPOSSIBLE")
