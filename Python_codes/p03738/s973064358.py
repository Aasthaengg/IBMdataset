import math
a = int(input())
b = int(input())
a = math.log10(a)
b = math.log10(b)
if a > b :
    print("GREATER")
elif a == b :
    print("EQUAL")
else :
    print("LESS")
