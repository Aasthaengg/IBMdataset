import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def check(k,ans):
    if k<2:
        print(ans+k)
        exit()

def main():
    k,a,b=MI()
    d=b-a
    if d<3:
        print(k+1)
        exit()
    ans=1
    cnt=min(a-1,k)
    ans+=cnt
    k-=cnt
    check(k,ans)
    cnt=k//2
    ans+=cnt*d
    k-=cnt*2
    check(k,ans)

main()