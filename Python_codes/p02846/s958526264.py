import math

T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

if (A1 - B1) * T1 + (A2 - B2) * T2 == 0:
    print("infinity")
else:
    D, D1 = (A1 - B1) * T1 + (A2 - B2) * T2, (A1 - B1) * T1
    if (D1 > 0) == (D > 0):
        print(0)
    else:
        if D1 % D == 0:
            print(2 * math.floor(-D1 / D))
        else:
            print(2 * math.floor(-D1 / D) + 1)
