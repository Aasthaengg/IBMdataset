import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    x,a,b=MI()
    if a>=b:
        print("delicious")
    elif a+x>=b:
        print("safe")
    else:
        print("dangerous")

main()
