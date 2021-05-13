import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    L=[[0,0,0]for _ in range(N)]
    for i in range(N):
        a,b=MI()
        L[i]=[a+b,a,b]
        
    L.sort(reverse=True)
    
    a=0
    b=0
    for i in range(N):
        if i%2==0:
            a+=L[i][1]
        else:
            b+=L[i][2]
            
    print(a-b)

main()
