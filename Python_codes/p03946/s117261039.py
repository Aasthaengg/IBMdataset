import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,T=MI()
    A=LI()
    M=[0]*N#自分以降の最大値
    M[-1]=A[-1]
    for i in range(1,N):
        M[-1-i]=max(M[-i],A[-i])
        
    diff=[0]*N
    for i in range(N):
        diff[i]=M[i]-A[i]
     
    diff.sort(reverse = True)
    ans=diff.count(diff[0])
    print(ans)

main()
