import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

def solve():
    n, k = nm()
    a = nl()
    ng = 0
    ok = max(a) + 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        cnt = 0
        for x in a:
            cnt += (x - 1)//mid
        if cnt > k:
            ng = mid
        else:
            ok = mid
    print(ok)
    return

solve()
