from sys import stdin

input = stdin.readline


MOD = 10**9 + 7



def solve():
    N = int(input())
    point = [tuple(map(int,inp.split())) for inp in stdin.read().splitlines()]
    pa = max(point,key = lambda x: x[0] + x[1])
    pb = min(point,key = lambda x: x[0] + x[1])
    pc = max(point,key = lambda x: x[0] - x[1])
    pd = min(point,key = lambda x: x[0] - x[1])
    r1 = pa[0] + pa[1] - pb[0] - pb[1]
    r2 = pc[0] - pc[1] + pd[1] - pd[0]
    print(max(r1,r2))
if __name__ == '__main__':
    solve()
