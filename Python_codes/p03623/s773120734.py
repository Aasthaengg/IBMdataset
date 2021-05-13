import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    x,a,b=MI()
    if abs(x-a)<abs(x-b):
        print("A")
    else:
        print("B")

main()
