import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    A,B,K=MI()
    
    for i in range(K):
        if i%2==0:
            A=A//2
            B+=A
        else:
            B=B//2
            A+=B
            
    print(A,B)

main()
