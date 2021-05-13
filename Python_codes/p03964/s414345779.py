import sys
INF = 10 ** 9
MOD = 10 ** 9 + 7
from collections import deque
sys.setrecursionlimit(100000000)


def main():
    n = int(input())
    senkyo = [tuple(map(int,input().split())) for _ in range(n)]
    
    last_t,last_a = senkyo[-1]
    
    def ok(x):
        t = x * last_t
        a = x * last_a
        flag = True
        for i in range(n - 2, -1, -1):
            ti,ai = senkyo[i]
            y = min(t//ti,a//ai)
            t = y * ti
            a = y * ai
            if a == 0 :
                flag = False
                break
        return flag
    
    r = 10 ** 18
    l = 0
    while r - l > 1:
        mid = (r + l)//2
        if ok(mid):
            r = mid
        else:
            l = mid
    
    print(r * (last_a + last_t))

if __name__=='__main__':
    main()


