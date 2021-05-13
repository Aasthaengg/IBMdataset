import math
A, B =map(int,input().split())

if A >=13 :
    print(B)
elif A >= 6 and 12 >=A :
    print(math.floor(B/2))
else : 
    print(0)