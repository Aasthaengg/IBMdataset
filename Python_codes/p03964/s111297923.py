import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    NT=1
    NA=1
    for i in range(N):
        T,A=MI()
        xt=(NT+T-1)//T
        xa=(NA+A-1)//A
        x=max(xt,xa)
        NT=T*x
        NA=A*x
    print(NT+NA)
            

main()
