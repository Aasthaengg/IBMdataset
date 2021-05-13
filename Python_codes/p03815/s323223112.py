import math 
x = int(input())
Su = math.floor(x/11)
M = x%11
if x < 11:
    if x <=6:
        print(1)
    else:
        print(2)
else:
    if M ==0:
        print(Su*2)
    else:
        if M <= 6:
            print(Su*2+1)
        else:
            print(Su*2+2)