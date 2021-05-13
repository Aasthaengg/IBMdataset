import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    N2=int(N**0.5)+5
    
    ans=0
    for i in range(1,N2):
        m=(N-i)//i
        if m*i+i==N:
            if i<m:
                ans+=m
                
    print(ans)

main()
