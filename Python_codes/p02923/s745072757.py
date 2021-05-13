import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    a=LI()+[10**10]
    ans=0
    now=-1
    cnt=0
    for i in range(N+1):
        if a[i]>now:
            ans=max(ans,cnt)
            cnt=0
        else:
            cnt+=1
        now=a[i]
        
    print(ans)
        

main()
