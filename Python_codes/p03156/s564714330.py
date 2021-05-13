import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A,B=MI()
    P=LI()
    P.sort()
    L=[0,0,0]
    for i in range(N):
        if P[i]<=A:
            L[0]+=1
        elif A+1<=P[i]<=B:
            L[1]+=1
        else:
            L[2]+=1
            
    print(min(L))
            
    

main()
