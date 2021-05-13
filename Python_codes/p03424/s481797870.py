n, *a = open(0).read().split()
b = len(set(a))
if b == 3:
    print("Three")
elif b == 4:
    print("Four")
