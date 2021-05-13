import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
    
        N,M=map(int,input().split())
        L=[0]*N
        for i in range(M):
            a,b=map(int,input().split())
            L[a-1]+=1
            L[b-1]+=1
        for i in range(N):
            if L[i]%2==1: return 'NO'
        return 'YES'
    print(main())
        


    
resolve()