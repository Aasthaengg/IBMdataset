import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    W,H,x,y=MI()
    ans=(W*H)/2
    if x==W/2 and y==H/2:
        print(ans,1)
    else:
        print(ans,0)
    
    

main()
