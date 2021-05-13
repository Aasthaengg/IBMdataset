import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    adj=[[]for _ in range(N)]
    for i in range(N-1):
        a,b=MI()
        a-=1
        b-=1
        adj[a].append(b)
        adj[b].append(a)
    c=LI()
    c.sort(reverse=True)    
    
    import queue
    q=queue.Queue()
    q.put(0)
    ans=[0]*N
    ans[0]=c[0]
    now=0
    
    while not q.empty():
        v=q.get()
        for nv in adj[v]:
            if ans[nv]==0:
                now+=1
                ans[nv]=c[now]
                q.put(nv)
                
    S=sum(c)-c[0]
    print(S)
    print(' '.join(map(str, ans)))
        

    

main()
