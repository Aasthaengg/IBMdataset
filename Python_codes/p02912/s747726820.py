import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    import heapq
    mod=10**9+7
    N,M=MI()
    A=LI()
    for i in range(N):
        A[i]*=-1
    heapq.heapify(A)
    
    for i in range(M):
        a=heapq.heappop(A)
        heapq.heappush(A,a/2)
        
    ans=0
    for i in range(N):
        a=heapq.heappop(A) * -1
        ans+=int(a)
        
    print(ans)
        

main()
