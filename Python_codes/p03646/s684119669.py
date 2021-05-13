import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    k=int(input())
    p,r=divmod(k,50)
    L=100+p-r
    R=49+p-r
    ans=[L]*r+[R]*(50-r)
    print(50)
    print(*ans)
main()