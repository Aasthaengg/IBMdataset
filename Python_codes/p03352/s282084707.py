import math
X = int(input())

def IsBekijo(x):
    if x == 1:
        return True
    for i in range(2,math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            d = x // i
            while d != 1:
                if d % i == 0:
                    d //=  i
                else:
                    break
            if d == 1:
                return True
    return False

for i in range(X,0, -1):
    if IsBekijo(i):
        print(i)
        break
