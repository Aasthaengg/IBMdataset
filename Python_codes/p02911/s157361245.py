import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K,Q=MI()
    L=[K-Q]*N
    for i in range(Q):
        a=I()
        a-=1
        L[a]+=1
        
    for i in range(N):
        if L[i]>0:
            print("Yes")
        else:
            print("No")

main()
