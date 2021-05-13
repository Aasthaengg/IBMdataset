import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

def solve():
    k = ni()
    c = 0
    for i in range(k):
        c = (c * 10 + 7) % k
        if c == 0:
            print(i+1)
            break
    else:
        print(-1)
    return

solve()
