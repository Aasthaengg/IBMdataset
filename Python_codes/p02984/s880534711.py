import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    S=sum(A)
    S2=0
    for i in range(1,N,2):
        S2+=A[i]
    
    B=[0]*N
    B[0]=S-S2*2
    for i in range(1,N):
        B[i]=A[i-1]*2-B[i-1]
        
    print(' '.join(map(str, B)))

main()
