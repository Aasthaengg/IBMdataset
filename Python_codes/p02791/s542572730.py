import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    P=LI()
    m=P[0]
    cnt=1
    for i in range(1,N):
        if P[i]<m:
            cnt+=1
            m=P[i]
            
    print(cnt)

main()