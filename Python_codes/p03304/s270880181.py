import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M,d=MI()
    temp=0
    if d==0 or 2*d>=N:
        temp=N
    else:
        temp=N+(N-2*d)
        
    ans=(temp/(N*N))*(M-1)
    print(ans)
    

main()
