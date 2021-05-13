import sys
from collections import deque
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    N=int(input())
    A=[[] for _ in range(N)]
    for i in range(N):
        A[i]=deque(list(map(lambda x: int(x)-1,input().split())))
    days=1
    c=0
    pre=[]
    tmp=[]
    for i in range(N):
        if A[i] and A[A[i][0]][0]==i:
            tmp.append(i)
            tmp.append(A[i][0])
    tmp=list(set(tmp))
    for i in tmp:
        A[i].popleft()
        c+=1
    pre=tmp
    if c<N*(N-1):
        while c<N*(N-1):
            tmp=[]
            for i in pre:
                if A[i] and A[A[i][0]][0]==i:
                    tmp.append(i)
                    tmp.append(A[i][0])
            tmp=list(set(tmp))
            for i in tmp:
                A[i].popleft()
                c+=1
            pre=tmp
            days+=1
            if days>N*(N-1)//2:
                print(-1)
                exit()
    print(days)
                
            
        
    
        
        

    

        
if __name__ == '__main__':
    main()
