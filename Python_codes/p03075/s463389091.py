import sys
rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.buffer.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.buffer.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

li = [ri() for _ in range(6)]
print(':(' if li[4] - li[0] > li[5] else 'Yay!')












