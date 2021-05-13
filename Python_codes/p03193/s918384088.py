import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,H,W=MI()
    ans=0
    for i in range(N):
        a,b=MI()
        if a>=H and b>=W:
            ans+=1
            
    print(ans)

main()
