import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=[0]*N
    Mi=-1
    M=0
    for i in range(N):
        A[i]=I()
        if A[i]>M:
            Mi=i
            M=A[i]
            
    A[Mi]=0
    
    for i in range(N):
        if i!=Mi:
            print(M)
        else:
            print(max(A))

main()
