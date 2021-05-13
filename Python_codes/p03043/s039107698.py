import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    ans=0
    for i in range(1,N+1):
        temp=1/N
        score=i
        while score<K:
            score*=2
            temp/=2
        ans+=temp
        
    print(ans)
    

main()
