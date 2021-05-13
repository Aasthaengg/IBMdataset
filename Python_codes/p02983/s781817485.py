import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=2019
    L,R=MI()
    
    if R-L>=2019:
        print(0)
        exit()
    a=L%mod
    b=R%mod
    if b<=a:
        print(0)
        exit()
    
    ans=mod
    for i in range(a,b+1):
        for j in range(i+1,b+1):
            temp=(i*j)%mod
            ans=min(ans,temp)
            
    print(ans)
            

main()
