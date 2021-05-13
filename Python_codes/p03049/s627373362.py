import sys,os
from collections import defaultdict, deque
from math import ceil, floor
if sys.version_info[1] >= 5:
    from math import gcd
else:
    from fractions import gcd
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    MOD = 10**9+7

    N = II()
    S = [0]*N
    numAB = 0
    numA = 0
    numB = 0
    ans = 0
    for i in range(N):
        s = input()
        ans += s.count('AB')
        if s[-1] == 'A':
            if s[0] == 'B':
                numAB += 1
            else:
                numA += 1
        elif s[0] == 'B':
            numB += 1



    if numA > 0 and numAB > 0:
        numA -= 1
        numAB += 1
    # elif numA == 0 and numAB > 0:
    #     numAB -= 1
    if numB > 0 and numAB > 0:
        numB -= 1
        numAB += 1
    # elif numB == 0 and numAB > 0:
    #     numAB -= 1
    if numAB > 0:

        ans += numAB -1  + min(numA,numB)
    else:
        ans += min(numA,numB)
    
        
    print(ans)
if __name__ == '__main__':
    main()