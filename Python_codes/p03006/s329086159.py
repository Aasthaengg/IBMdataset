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
    coordinates = []
    diffs = defaultdict(int)
    for i in range(N):
        coordinates.append(LMIIS())
    coordinates.sort()
    for i in range(N):
        x1,y1 = coordinates[i]
        for j in range(i+1,N):
            x2,y2 = coordinates[j]
            diffs[(x1-x2,y1-y2)] += 1
    
    max_diff = ()
    max_count = 0

    for k,v in diffs.items():
        if max_count < v:
            max_count = v
            max_diff = k
    print(N-max_count)


if __name__ == '__main__':
    main()