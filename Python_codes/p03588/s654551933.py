import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    temp=0
    ans=0
    for i in range(N):
        a,b=MI()
        if a>temp:
            ans=a+b
            temp=a
            
    print(ans)

main()
