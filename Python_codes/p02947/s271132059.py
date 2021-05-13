
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    from collections import defaultdict
    dd = defaultdict(int)
    
    for _ in range(N):
        s=list(input())
        s.sort()
        s=''.join(map(str, s))
        dd[s]+=1
        
    ans=0
    
    for k,v in dd.items():
        ans+=(v*(v-1))//2
        
    print(ans)

main()
