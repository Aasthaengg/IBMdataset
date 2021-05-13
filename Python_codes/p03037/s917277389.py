import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    L=[0]*(N+1)
    for _ in range(M):
        l,r=MI()
        l-=1
        r-=1
        L[l]+=1
        L[r+1]-=1
        
    for i in range(N):
        L[i+1]+=L[i]
        
    ans=0
    
    for i in range(N):
        if L[i]>=M:
            ans+=1
            
    print(ans)
    

main()
