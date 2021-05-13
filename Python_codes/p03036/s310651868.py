def x_i(r,D,x):
    return r*x-D

try:
    r,D,x_2000=map(int, input().split())
    assert 2<=r<=5 and 1<=D<=100 and D<x_2000<=200

    for i in range(2001,2011):
        print(r*x_2000-D)
        x_2000=r*x_2000-D
except AssertionError:
    print('')

