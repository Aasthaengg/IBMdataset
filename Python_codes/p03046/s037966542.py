import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    M,K=MI()
    N=pow(2,M)
    
    if K>=N or (M==1 and K==1):
        print(-1)
    elif M==1 and K==0:
        print(0,0,1,1)
    else:
        from collections import deque
        dq=deque()
        dq.append(K)
        for i in range(N):
            if i!=K:
                dq.append(i)
                dq.appendleft(i)
        dq.append(K)
        
        ans=[]
        while len(dq)!=0:
            ans.append(dq.pop())
        print(' '.join(map(str, ans)))
    

                

main()
