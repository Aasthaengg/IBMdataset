import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,A,B=MI()
    ans=0
    rem=N-2
    ans=rem*(B-A)+1
    ans=max(ans,0)
    if A>B or (rem<0 and B-A>=1):
        ans=0
    print(ans)

main()
