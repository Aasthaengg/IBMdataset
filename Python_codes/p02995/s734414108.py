import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    a,b,c,d=MI()
    cc=b//c - (a-1)//c
    dd=b//d - (a-1)//d
    
    import math
    g=(c*d)//math.gcd(c,d)
    gg=b//g - (a-1)//g
    
    print(b-a+1 -cc-dd+gg)

main()
