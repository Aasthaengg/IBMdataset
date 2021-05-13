
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    AC=[0]*N
    WA=[0]*N
    
    for _ in range(M):
        p,s=input().split()
        p=int(p)-1
        if s=="AC":
            AC[p]=1
        else:
            if AC[p]==0:
                WA[p]+=1
       
    acs=sum(AC)     
    was=0
    for i in range(N):
        was+=AC[i]*WA[i]
        
    print(acs,was)
        

main()
