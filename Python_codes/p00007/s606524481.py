import math

if __name__ == '__main__':
    n = (int)(input())
    a = 100000
    for x in range(0,n):
        b = a*1.05
        c = math.ceil(b/1000)
        a = c*1000
    print(a)