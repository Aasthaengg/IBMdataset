import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    import math
    mod=10**9+7
    a,b,x3=MI()
    
    x=x3/(a**2) #引数勘違いしてた
    
    if (a*b)//2 >= a*x :
        y=(2*a*x)/b
        th=math.atan2(b,y)
        
    else:
        rem=a*(b-x)
        z=rem*2/a
        th=math.atan2(z,a)
        
    print(th/math.pi * 180)
        

main()
