import math
a, b = input().split()
c = a+ b
if a == b == "100":
    print("No")
    exit()
if pow(math.sqrt(int(c)), 2) == int(c):
    print("Yes")
else:
    print("No")