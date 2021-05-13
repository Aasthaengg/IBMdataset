import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    ans=pow(3,N)
    cnt=1
    for i in range(N):
        if A[i]%2==0:
            cnt*=2
            
    print(ans-cnt)

main()
