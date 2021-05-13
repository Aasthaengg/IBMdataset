#ABC056 A

a,b = input().split()
if a == "H":
    a = 1
else:
    a = -1
if b == "H":
    b = 1
else:
    b = -1
if a*b == 1:
    print("H")
else:
    print("D")