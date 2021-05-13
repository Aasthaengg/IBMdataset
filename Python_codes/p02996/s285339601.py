import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    Q=[]
    for _ in range(N):
        a,b=MI()
        Q.append([b,a])
        
    Q.sort()
    now=0
    flag=1
    for i in range(N):
        b,a=Q[i]
        now+=a
        if now>b:
            flag=0
            break
            
    if flag:
        print("Yes")
    else:
        print("No")
        

main()
