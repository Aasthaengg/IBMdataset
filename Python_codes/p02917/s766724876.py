import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    B=LI()
    A=[0]*N
    A[0]=B[0]
    A[-1]=B[-1]
    for i in range(N-2):
        A[i+1]=min(B[i],B[i+1])
        
    print(sum(A))

main()
