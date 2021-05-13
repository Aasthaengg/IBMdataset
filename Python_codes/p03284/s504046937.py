import math
a,b = map(int,input().split())
maxi = math.ceil(a/b)
minu = math.floor(a/b)
print(maxi - minu)