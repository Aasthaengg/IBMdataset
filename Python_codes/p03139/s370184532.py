import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,A,B=MI()
    a=min(A,B)
    b=max((A+B)-N,0)
    print(a,b)

main()