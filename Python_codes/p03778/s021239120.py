import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    W,a,b=MI()
    d1=max(0,b-(a+W))
    d2=max(0,a-(b+W))
    print(max(d1,d2))

main()
