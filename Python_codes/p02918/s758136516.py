
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    S=input()
    
    ans=0
    now="A"
    for i in range(N):
        if S[i]==now:
            ans+=1
        now=S[i]
    
    ans=(min(N-1,ans+K*2))
    print(ans)
        

main()
