import math
N=int(input())
s=N/1.08
s=math.ceil(s)
t=s*1.08
t=math.floor(t)
if N==t:
    print(s)
else :
    print(":(")
