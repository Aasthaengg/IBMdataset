import math
a,b=map(str,input().split())
a=int(a+b)
if math.sqrt(a)==int(math.sqrt(a)):print("Yes")
else:print("No")