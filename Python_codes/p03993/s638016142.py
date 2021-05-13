import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    n=int(input())
    A=list(map(int,input().split()))
    cnt=0
    for i in range(n):
        if A[A[i]-1]==i+1:
            cnt+=1
    print(cnt//2)    
resolve()