a,b = input().split()
import math
S = int(a+b)

if math.sqrt(S).is_integer() == True:
    print("Yes")
else:
    print("No")