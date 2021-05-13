def GCD(x,y):

    if(x >= y):
        z = y
        w = x%y
    else:
        z = x
        w = y%x

    if(not(w == 0)):
        return GCD(z,w)
    else:
        return z

A = [int(i) for i in input().split()]
print(GCD(A[0],A[1]))

"""実行結果

100 55
5



66 77
11

"""

