import math
x = int(input())
ans = x//11
ans2 = x%11
if x <= 6:
    print(1)
elif x<=11:
    print(2)
else:
    if x%11 == 0:
        print(ans*2)
    else:
        if ans2 > 6:
            print(ans*2+2)
        else:
            print(ans*2+1)
