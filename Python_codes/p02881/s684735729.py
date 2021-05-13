import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    ans=N
    
    M=10**6+5
    for i in range(1,M):
        if N%i==0:
            j=N//i
            temp=i+j-2
            ans=min(ans,temp)
            
    print(ans)
            
        

main()
