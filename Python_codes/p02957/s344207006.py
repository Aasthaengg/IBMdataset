import math
a,b = map(int,input().split())
if (max(a,b) - min(a,b)) % 2 == 0:
    print(math.floor((a+b)/2))
else:
    print("IMPOSSIBLE")