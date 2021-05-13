import math
a,b = map(int,input().split())
flg = 1

for i in range(1,1001):
    x1 = math.floor(i*0.08)
    x2 = math.floor(i*0.10)
    if x1 == a and x2 == b:
        print(i)
        flg = 0
        break
    else:
        pass
    
if flg:
    print(-1)