import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    b=LI()
    ans=[]
    for _ in range(N):
        for i in range(len(b)-1,-1,-1):
            if b[i]==i+1:
                ans.append(b[i])
                b.pop(i)
                break
            
    if len(ans)==N:
        for i in range(N):
            print(ans[-1-i])
    else:
        print(-1)
        

main()
