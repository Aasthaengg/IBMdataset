import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    N=int(input())
    A=[0]+list(map(int,input().split()))
    ans=[0]*(N+1)
    s=[0]*(N+1)

    for i in reversed(range(1,N+1)):
        cnt=0
        for j in range(i+i,N+1,i):
            cnt^=s[j]
        if (A[i]==1 and cnt!=1) or (A[i]==0 and cnt!=0): s[i]=1
    
    print(sum(s))
    for i in range(1,N + 1):
        if s[i]==1:
            print(i)






    

resolve()