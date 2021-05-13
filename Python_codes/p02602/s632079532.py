import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    A=LI()
    ans=[]
    for i in range(K,N):
        if A[i]>A[i-K]:
            ans.append("Yes")
        else:
            ans.append("No")
            
    for s in ans:
        print(s)

main()
