import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    import queue
    mod=10**9+7
    N,K=MI()

    #0~Nまで逆元などを事前計算

    def calc(n, r, mod):
        if (r < 0) or (n < r):
            return 0
        return (fact[n] * factinv[n-r])%mod

    fact=[1,1]
    factinv=[1,1]
    inv=[0,1]

    for i in range(2, 10**5+5 + 1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)
    
    adj=[[]for _ in range(N)]
    for i in range(N-1):
        a,b=MI()
        a-=1
        b-=1
        adj[a].append(b)
        adj[b].append(a)
    
    #子要素を全部いっぺんに塗る
    ans=K#根の塗り方
    
    q=queue.Queue()
    q.put((0,0,-1))
    
    while not q.empty():
        v,d,p=q.get()
        cnt=0#子の個数
        for nv in adj[v]:
            if nv!=p:
                cnt+=1
                q.put((nv,d+1,v))
            
        if cnt!=0:#葉以外の場合は計算
            np=2#親方向で気にすべき個数
            if d==0:
                np=1#根の親はいない
                
            ans=(ans*calc(K-np,cnt,mod))%mod
        
    print(ans)

        
    

main()
