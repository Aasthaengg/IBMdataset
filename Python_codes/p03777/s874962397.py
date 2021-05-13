a, b = input().split()
a = (a == "H")
b = (b == "H")
if a and b:
    print("H")
elif a and (not b):
    print("D")
elif (not a) and b:
    print("D")
else:
    print("H")