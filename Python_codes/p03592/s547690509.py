import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M,K=MI()
    flag=0
    
    for i in range(N+1):
        for j in range(M+1):
            temp=i*M+j*N-(i*j)*2
            if temp==K:
                flag=1
                break
            
            
    if flag:
        print("Yes")
    else:
        print("No")

main()
