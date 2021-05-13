import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    cnt=0
    N=int(input())
    for i in range(N):
        l,r=map(int,input().split())
        cnt+=r-l+1
    print(cnt)

resolve()