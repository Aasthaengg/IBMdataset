import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    H=LI()
    
    now=0
    
    for i in range(N):
        if H[i]!=now:
            H[i]-=1
        now=H[i]
    
    flag=1
    now=0
    for i in range(N):
        if H[i]<now:
            flag=0
            break
        now=H[i]
        
    if flag:
        print("Yes")
    else:
        print("No")
            

main()
