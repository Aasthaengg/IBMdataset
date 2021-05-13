import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    x,y=MI()
    if x%y==0:
        print(-1)
    else:
        print(x*(y+1))

main()
