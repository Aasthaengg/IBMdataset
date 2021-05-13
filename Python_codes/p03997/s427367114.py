import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    a=I()
    b=I()
    h=I()
    print(((a+b)*h)//2)

main()
