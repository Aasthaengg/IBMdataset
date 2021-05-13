from fractions import gcd

def func():
    x,y=map(int,input().split())
    if gcd(x,y) == y:
        print("-1")
    else :
        print(x)

func()
