import math
X = int(input())
if X == 2 or X == 3:
    print(X)
else:

 while True:
    for i in range(2,int(math.sqrt(X))):
       Flag = True
       if X % i == 0:
           Flag = False
           break
    if Flag:
        break
    X += 1
 print(X)