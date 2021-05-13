import math
a, b = map(int,input().split())
ab = int(str(a) + str(b))
if int(math.sqrt(ab))**2 == ab :
    print('Yes')
else :
    print('No')