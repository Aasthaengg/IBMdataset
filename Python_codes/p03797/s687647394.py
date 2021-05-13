import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    
    if M>2*N:
        M+=N*2
        print(M//4)
    else:
        print(min(N,M//2))

main()
