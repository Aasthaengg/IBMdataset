import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    P=LI()
    S=[0]*(N+1)
    
    for i in range(N):
        S[i+1]=S[i]+P[i]
        
    M=0
    for i in range(N-K+1):
        temp=S[K+i]-S[i]
        M=max(M,temp)
        
    ans=(M+K)/2
    print(ans)

main()
