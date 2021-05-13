import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    a=I()
    b=I()
    
    if a==b:
        print("EQUAL")
    elif a>b:
        print("GREATER")
    else:
        print("LESS")

main()
