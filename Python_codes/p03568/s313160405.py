import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    N=int(input())
    A=list(map(int,input().split()))

    ans=1
    for i in range(N):
        if A[i]%2==0:
            ans*=2
    print(3**N-ans)
    
resolve()