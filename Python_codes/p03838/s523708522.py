import numpy as np
x, y = map(int, input().split())

if(abs(x) >= abs(y)):
    if(np.sign(x) == np.sign(y)):
        if(np.sign(x) < 0):
            print(abs(x)-abs(y))
        else:
            print(2+abs(x)-abs(y))
    else:
        if(y != 0):
            print(1+abs(x)-abs(y))
        else:
            if(x < 0):
                print(abs(x))
            else:
                print(1+abs(x))
else:
    if(np.sign(x) == np.sign(y)):
        if(np.sign(x) > 0):
            print(abs(y)-abs(x))
        if(np.sign(x) < 0):
            print(2+abs(y)-abs(x))
    else:
        if(x == 0):
            if(y > 0):
                print(abs(y))
            else:
                print(1+abs(y))
        else:
            print(1+abs(y)-abs(x))