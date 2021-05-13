import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    a,b,c=MI()
    f=0
    if b-a==c-b:
        f=1
        
    if f==1:
        print("YES")
    else:
        print("NO")

main()
