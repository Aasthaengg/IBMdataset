import sys
sys.stdin.readline
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
mod=10**9+7

def main():
    N=I()
    A=[0]*N
    B=[0]*N
    for i in range(N):
        A[i],B[i]=MI()
        
    ans=0
    for i in range(N-1,-1,-1):
        A[i]+=ans
        target=(((A[i]+B[i]-1)//B[i]))*B[i]
        ans+=target-A[i]
        
    print(ans)
            
    


main()