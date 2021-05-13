import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    a,b,x = LI()
    ok = 0
    ng = 90

    while ng - ok >= 10**(-8):
        middle = (ng+ok) /2
        volume = 0

        if a*math.tan(math.radians(middle)) <= b:
            volume = a**2*b - a**3*math.tan(math.radians(middle))/2
        else:
            volume = a*b**2/(2*math.tan(math.radians(middle)))
        if volume >= x:
            ok = middle
        else:
            ng = middle
    
    ans = ok
    print(ans)
main()
