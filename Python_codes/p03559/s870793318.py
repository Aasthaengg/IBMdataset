import sys, os
import bisect

f = lambda:list(map(int,input().split()))
if 'local' in os.environ :
    sys.stdin = open('./input.txt', 'r')

def solve():
    n = f()[0]
    a = f()
    b = f()
    c = f()

    a = sorted(a)
    b = sorted(b)
    c = sorted(c)

    ans = 0
    for i in range(n):
        mid = b[i]
        ans += bisect.bisect_left(a, mid) *(n- bisect.bisect_right(c, mid))
    
    print(ans)


    

solve()
