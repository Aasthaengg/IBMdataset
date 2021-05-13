import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    L=list(input())
    N=len(L)
    
    #桁dp
    dpl=[0]*(N+1)
    dpt=[0]*(N+1)
    dpt[0]=1
    
    
    for i in range(N):
        if L[i]=="1":
            dpl[i+1]=(dpl[i]*3+dpt[i])%mod#00,01,10,  00
            dpt[i+1]=(dpt[i]*2)%mod
        else:
            dpl[i+1]=(dpl[i]*3)%mod#00,01,10
            dpt[i+1]=dpt[i]
            
    ans=(dpl[-2]+dpt[-2])%mod
    print(ans)
            
            
            

main()
