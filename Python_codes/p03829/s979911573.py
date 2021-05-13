import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,A,B=MI()
    X=LI()
    ans=0
    for i in range(N-1):
        d=X[i+1]-X[i]
        ans+=min(d*A,B)
        
    print(ans)

main()
