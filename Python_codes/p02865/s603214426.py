import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    ans=0
    for i in range(1,N):
        j=N-i
        if i!=j:
            ans+=1
    print(ans//2)
        
        

main()
