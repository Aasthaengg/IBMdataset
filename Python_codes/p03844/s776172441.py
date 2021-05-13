import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    a,op,b=input().split()
    if op=="+":
        print(int(a)+int(b))
    else:
        print(int(a)-int(b))

main()
