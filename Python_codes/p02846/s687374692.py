INF = 10 ** 9
MOD = 10 ** 9 + 7
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from  math import factorial


def main():
    t1,t2 = map(int,input().split())
    a1,a2 = map(int,input().split())
    b1,b2 = map(int,input().split())
    if (a1 - b1) * t1 + (a2 - b2) * t2 == 0:
        ans = 'infinity'
    elif a1 == b1 or a2 == b2:
        ans = 'infinity'
    elif (a1 < b1 and a2 < b2) or (a1 > b1 and a2 > b2):
        ans = 0
    else:
        if a1 > b1 and a2 < b2:
            a1,b1 = b1,a1
            a2,b2 = b2,a2
        if (b1 - a1) * t1 + (b2 - a2) * t2 > 0:
            ans = 0
        else:
            x = (a1 - b1) * t1 + (a2 - b2) * t2
            if (b1 * t1 - a1 * t1) < x:
                ans = 1
            elif (b1 * t1 - a1 * t1)%x == 0:
                ans = 1 + 2 * ((b1 * t1 - a1 * t1)//x - 1) + 1
            else:
                ans = 1 + 2 * ((b1 * t1 - a1 * t1)//x)
    print(ans)
if __name__ == '__main__':
    main() 