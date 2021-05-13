import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    A=LI()
    
    ng=0
    ok=10**9
    
    def f(x):
        temp=0#切る回数
        for i in range(N):
            temp+=(A[i]-0.1)//x
        
        return temp<=K
    
    while ok-ng>1:
        med=(ok+ng)//2
        if f(med):
            ok=med
        else:
            ng=med
               
    print(ok)
    

main()
