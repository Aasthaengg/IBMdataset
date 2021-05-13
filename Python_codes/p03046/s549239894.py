import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    M,K=MI()
    N=pow(2,M)
    if K>=N:
        print(-1)
        exit()
    elif M==1 and K==0:
        print(0,0,1,1)
    else:
        ans=[]
        temp=0
        for i in range(N):
            if i!=K:
                ans.append(i)
                temp=temp^i
        ans.append(K)
        for i in range(N-1,-1,-1):
            if i!=K:
                ans.append(i)
        ans.append(K)
        if temp!=K:
            print(-1)
        else:
            print(' '.join(map(str, ans)))        

                

main()
