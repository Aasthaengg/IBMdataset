import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    #最大個数はスターグラフ，辺を追加すれば減らせる
    
    N2=((N-1)*(N-2))//2
    
    if K>N2:
        print(-1)
        exit()
    
    E=[]
    for i in range(1,N):
        E.append([0,i])#0が中心
        
    rem=N2-K
    
    for i in range(1,N):
        for j in range(i+1,N):
            if rem==0:
                break
            E.append([i,j])
            rem-=1
            
    M=len(E)
    print(M)
    
    for u,v in E:
        print(u+1,v+1)
            
    
    
            
    

main()
