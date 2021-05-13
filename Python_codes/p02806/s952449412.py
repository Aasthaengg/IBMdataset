import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    N=int(input())
    
    A, B = [0] * N, [0] * N
    for i in range(N):
        A [i], x = map(str, input().split())
        B[i]=int(x)
    X=str(input())
    for i in range(N):
        if A[i]==X:
            print(sum(B[i+1:]))
            break
    

    

    

    
resolve()