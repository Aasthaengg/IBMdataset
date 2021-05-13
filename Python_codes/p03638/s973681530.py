import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    h,w=MI()
    n=int(input())
    aa=LI()
    i=j=0
    ans=[[0]*w for _ in range(h)]
    for c,a in enumerate(aa,1):
        for _ in range(a):
            ans[i][j]=c
            if i%2:j-=1
            else:j+=1
            if j==-1:
                i+=1
                j=0
            if j==w:
                i+=1
                j=w-1
    for ar in ans:
        print(*ar)
main()