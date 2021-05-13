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
    robots = [0]*N
    for i in range(N):
        x, l = map(int,input().split())
        left = x-l
        right = x+l
        robots[i]=(right,left)
    robots.sort()
    dbg(robots)
    prev_right = robots[0][0]

    ans = 1
    for i in range(1,N):
        if prev_right <= robots[i][1]:
            prev_right = robots[i][0]
            ans += 1
    print(ans)



    

if __name__ == '__main__':
    main()