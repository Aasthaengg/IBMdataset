#--coding:utf-8

def gcd(x, y):
    if x < y:
        gcd(y,x)
    if x%y == 0:
        return y 
    else:
        return gcd(y, x%y)

x, y = map(int, raw_input().split())
print gcd(x, y)