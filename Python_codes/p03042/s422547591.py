s = input()

i1 = int(s[:2])
i2 = int(s[2:])



def f(i):
    if (0 < i < 13):
        return 1
    elif (0 < i < 100):
        return 2
    else:
        return 0


f1 = f(i1)
f2 = f(i2)

if (f1 == 1):
    if (f2 == 1):
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if (f2 == 1):
        print("YYMM")
    else:
        print("NA")


