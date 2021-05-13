import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

def solve():
    h, w, k = nm()
    g = [ns() for _ in range(h)]
    ans = 0
    for bih in range(1 << h):
        for biw in range(1 << w):
            cnt = 0
            for i in range(h):
                for j in range(w):
                    if bih & (1 << i) and biw & (1 << j) and g[i][j] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)
    return

solve()
