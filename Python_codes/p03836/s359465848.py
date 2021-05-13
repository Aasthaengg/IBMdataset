import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    sx, sy, tx, ty = map(int, readline().split())
    dx = tx-sx
    dy = ty -sy
    ans = ('U'*dy+'R'*dx)+ ('D'*dy+'L'*dx)+('L'+'U'*(dy+1)+'R'*(dx+1)+'D')+('R'+'D'*(dy+1)+'L'*(dx+1)+'U')
    print(ans)
if __name__ == '__main__':
    main()