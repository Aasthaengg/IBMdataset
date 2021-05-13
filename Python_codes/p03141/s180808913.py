import sys
import numpy as np
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


def main():
    n = ii()
    x = []  
    ans = 0     
    for i in range(n):
        a, b = mi()
        x.append(a+b)
        ans -= b
    x.sort(reverse=True)
    ans += sum(x[::2])    
    print(ans)






if __name__ == '__main__':
    main()