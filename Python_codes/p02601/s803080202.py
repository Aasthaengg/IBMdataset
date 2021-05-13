import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    a,b,c=MI()
    K=I()
    cnt=0
    while b<=a:
        b*=2
        cnt+=1
        
    while c<=b:
        c*=2
        cnt+=1
        
    if cnt<=K:
        print("Yes")
    else:
        print("No")

main()
