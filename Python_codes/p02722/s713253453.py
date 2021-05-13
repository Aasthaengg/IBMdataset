#coding:utf-8
import sys,os
from collections import defaultdict, deque
from fractions import gcd
from math import ceil, floor
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    XLMIIS = lambda x: [LMIIS() for _ in range(x)]
    YN = lambda c : print('Yes') if c else print('No')
    MOD = 10**9+7

    N = II()
    def divisors(x):
        r1 = deque()
        r2 = deque()
        for i in range(1,ceil(x**0.5)):
            if x % i == 0:
                r1.append(i)
                r2.appendleft(x//i)
        if int(x**0.5) == x**0.5:
            r1.append(int(x**0.5))
        return list(r1)+list(r2)
    #N-1の約数
    ans = len(divisors(N-1))-1
    # print(ans)
    # print(divisors(N))
    for d in divisors(N)[1:]:
        tmpN = N
        while tmpN % d == 0:
            tmpN //= d
        if tmpN % d == 1:
            ans += 1

            
            
    print(ans)


    

if __name__ == '__main__':
    main()