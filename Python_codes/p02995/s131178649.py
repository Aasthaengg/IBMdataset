import numpy
a,b,c,d= list(map(int, input().strip().split()))
e=numpy.lcm(c,d)
def kosuu(x):
    return(b//x-(a-1)//x)
print(b-a+1-kosuu(c)-kosuu(d)+kosuu(e))