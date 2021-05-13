import sys
def I(): return int(sys.stdin.readline().rstrip())
H,W,N = [I() for _ in range(3)]
print(-(-N//max(H,W)))
