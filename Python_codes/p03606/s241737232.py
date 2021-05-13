import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    ans=0
    for i in range(N):
        l,r=MI()
        ans+=(r-l)+1
        
    print(ans)

main()
